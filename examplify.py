# this is a horribly hacky script.
# the idea is to override the browser opening action in webweb examples
import sys
import argparse
import os
import importlib.util
import webbrowser
import json
from collections import defaultdict
import yaml
import shutil
import re

DEFAULT_INPUT_DIR = os.path.join(os.getcwd(), 'webweb', 'examples')
DEFAULT_DATA_OUTPUT_DIR = os.path.join(os.getcwd(), '_data', 'examples')
DEFAULT_PAGES_OUTPUT_DIR = os.path.join(os.getcwd(), 'docs', 'examples')

def make_examples(input_dir, data_output_dir, pages_output_dir):
    examples_map = get_examples_map(input_dir)

    for number, (name, language_file_map) in enumerate(sorted(examples_map.items())):
        ex = Example(name, language_file_map, example_number=number + 1)
        ex.write(page_directory=pages_output_dir, data_directory=data_output_dir)

class Example(object):
    def __init__(self, name, language_to_file_map, example_number):
        self.name = name
        self.language_to_file_map = language_to_file_map
        self.example_number = example_number

        self.read()

    def create_output_directories(self):
        # set up the data directory
        if not os.path.exists(self.data_directory_name):
            os.mkdir(self.data_directory_name)

        # set up the representation directory
        if not os.path.exists(self.representations_directory_name):
            os.mkdir(self.representations_directory_name)

    @property
    def page_file_name(self):
        return os.path.join(self.page_directory, self.name + '.md')

    @property
    def data_directory_name(self):
        return os.path.join(self.data_directory, self.name)

    @property
    def representations_directory_name(self):
        return os.path.join(self.data_directory_name, 'representations')

    def read(self):
        self.read_json()
        self.read_representations()

    @property
    def pretty_json(self):
        # we need two kinds of json:
        # 1. raw json (for supplying to the webweb visualization of the example)
        # 2. pretty json (for displaying in case someone is curious)
        return json.dumps(self.json, indent=4, sort_keys=True)

    def read_json(self):
        # override the webbrowser so we don't have to open it
        webbrowser.open_new = lambda _: None

        # load the example
        spec = importlib.util.spec_from_file_location(self.name, self.language_to_file_map['python'])
        example_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(example_module)

        self.json = json.loads(example_module.web.json)

    def read_representations(self):
        """this function returns a dictionary with data displayed in the code switcher"""
        self.representations = {}
        for lang_name, lang_file_path in self.language_to_file_map.items():
            with open(lang_file_path, 'r') as f:
                lang_code = f.readlines()

            # remove trailing newline
            lang_code[-1] = lang_code[-1].rstrip()

            self.representations[lang_name] = lang_code

        # add the pretty json for displaying
        self.representations['json'] = self.pretty_json

    def write(self, page_directory, data_directory):
        self.page_directory = page_directory
        self.data_directory = data_directory
        self.create_output_directories()
        self.write_data()
        self.write_page()

    def change_webweb_json_for_display(self):
        self.json['display']['showWebOnly'] = True
        self.json['display']['attachWebToElementWithId'] = self.webweb_visualization_id

    def write_data(self):
        self.change_webweb_json_for_display()

        # write the json
        fn = os.path.join(self.data_directory_name, 'json.json')
        with open(fn, 'w') as f:
            json.dump(self.json, f, indent=4, sort_keys=True)

        # write each representation
        for representation_name, content in self.representations.items():
            fn = os.path.join(
                self.representations_directory_name,
                self.writeable_representation(representation_name) + '.json'
            )

            with open(fn, 'w') as f:
                json.dump(content, f, indent=4, sort_keys=True)

    def write_page(self):
        with open(self.page_file_name, 'w') as f:
            f.write('---\n')
            f.write(yaml.dump(self.page_frontmatter, default_flow_style=False))
            f.write('\n---\n\n')

            f.write(self.page_content)

    @property
    def page_frontmatter(self):
        return {
            'title' : self.name.replace('_', ' '),
            'layout' : 'home',
            'parent' : 'examples',
            'nav_order' : self.example_number,
        }

    def get_representations_select(self):
        # we always have python code so to be consistent we will show:
        # - python first
        # - json last
        representation_ordering = ['python', 'python (networkx)', 'matlab', 'json']

        ordered_representations = [rep for rep in representation_ordering if self.representations.get(rep)]

        select_include = '{{% include code_switcher.html code_options="{options}" %}}'.format(
            options="---".join(ordered_representations)
        )

        representation_options = []
        for representation in ordered_representations:
            representation_options.append(self.get_representation_select_option(representation))

        options = "\n".join(representation_options)

        return "\n".join([select_include, options])

    def writeable_representation(self, representation):
        return re.sub(r'\W+', '', representation.replace(' ', '_'))

    def get_representation_select_option(self, representation):
        writeable_representation = self.writeable_representation(representation)

        representation_content_path = 'site.data.examples.{name}.representations.{representation}'.format(
            name=self.name,
            representation=writeable_representation,
        )

        language = representation

        if representation == 'python (networkx)':
            language = 'python'

        content = "```{language}\n{{{{{content_path}}}}}\n```".format(
            language=language, 
            content_path=representation_content_path,
        )

        representation_display_classes = ["select-code-block"]

        # make python visible
        if representation == 'python':
            representation_display_classes.append("select-code-block-visible")

        div = "<div id='{representation}-code-block' class='{class_string}'></div>".format(
            representation=writeable_representation,
            class_string=" ".join(representation_display_classes),
        )

        return "\n".join([div, content])

    @property
    def webweb_visualization_id(self):
        return "webweb-example-visualization"

    def get_webweb_visualization(self):
        div = "<div id='{}' style='width: 100%'></div>".format(self.webweb_visualization_id)

        visualization = "{{% assign webweb_json=site.data.examples.{name}.json | jsonify %}}\n".format(name=self.name)
        visualization += "{% include webweb_dependencies.html webweb_json=webweb_json %}\n"

        return "\n".join([div, visualization])

    @property
    def page_content(self):
        return "\n".join([
            self.get_webweb_visualization(),
            self.get_representations_select(),
        ])

def prepare_data_output_dir(data_output_dir):
    """makes the data directory if it doesn't exist
    cleans the data directory if it does"""
    if not os.path.exists(data_output_dir):
        os.mkdir(data_output_dir)
        return

    for thing in os.listdir(data_output_dir):
        thing_path = os.path.join(data_output_dir, thing)

        if os.path.isdir(thing_path):
            shutil.rmtree(thing_path)

def prepare_pages_output_dir(pages_output_dir):
    """makes the pages directory if it doesn't exist
    cleans the pages directory if it does"""
    if not os.path.exists(pages_output_dir):
        os.mkdir(pages_output_dir)
        return

    example_pages = os.listdir(pages_output_dir)

    example_pages = [p for p in example_pages if p != 'examples.md']

    for page in os.listdir(pages_output_dir):
        # we don't want to remove the index file
        if page == 'examples.md':
            continue

        page_path = os.path.join(pages_output_dir, page)
        os.unlink(page_path)


def get_examples_map(input_dir):
    """generate a dictionary of examples to the code for each language and the file
    eg: {
        'simple' : {
            'python' : 'python/simple.py',
            'matlab' : 'matlab/simple.m',
        },
        ...
    }
    """
    file_map = defaultdict(dict)
    for dir_name, subdir_names, file_names in os.walk(input_dir):
        for file_name in file_names:
            name, ext = os.path.splitext(file_name)
            if ext in ['.py', '.m']:
                language = os.path.basename(dir_name)
                file_map[name][language] = os.path.join(dir_name, file_name)

    return file_map

if __name__ == '__main__':
    print('TODO: fix code copying from webweb')
    # mkdir assets/js/webweb/client
    # mkdir assets/css/webweb/client

    # cp webweb/webweb/client/js assets/js/webweb/client
    # cp webweb/webweb/client/css assets/css/webweb/client
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', '-i', default=DEFAULT_INPUT_DIR, help="the directory to generate examples from")
    parser.add_argument('--data_output_dir', '-d', default=DEFAULT_DATA_OUTPUT_DIR, help="the directory to output example data to")
    parser.add_argument('--pages_output_dir', '-p', default=DEFAULT_PAGES_OUTPUT_DIR, help="the directory to output example pages to")

    args = parser.parse_args()

    prepare_data_output_dir(args.data_output_dir)
    prepare_pages_output_dir(args.pages_output_dir)

    make_examples(args.input_dir, args.data_output_dir, args.pages_output_dir)
