# this script does beautiful and useful things, but they can only be done in ugly ways.
# the idea is to override the browser opening action in webweb examples

from collections import defaultdict
import importlib.util
import json
import os
import re
import shutil
import sys
import webbrowser

import util

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
            if ext in ['.md', '.py', '.m']:
                language = os.path.basename(dir_name)
                file_map[name][language] = os.path.join(dir_name, file_name)

    return file_map

def examplify(input_dir, data_output_dir, pages_output_dir, collection_name, nav_order=0):
    util.clean_dir(pages_output_dir)
    util.clean_dir(data_output_dir)

    examples_map = get_examples_map(input_dir)

    index = util.Page(
        title=collection_name,
        writeable_title=collection_name,
        nav_order=nav_order,
        layout='main_page',
        has_children=True,
        permalink='/{0}/'.format(collection_name),
    )

    index.write(pages_output_dir)

    ordered_examples_map = sorted(examples_map.items(), key=lambda x: x[0])

    for i, (name, language_file_map) in enumerate(ordered_examples_map):
        ex = Example(name, language_file_map, parent=collection_name, example_number=i + 1)
        ex.write(page_directory=pages_output_dir, data_directory=data_output_dir)

class Example(object):
    def __init__(self, writeable_name, language_to_file_map, parent, example_number):
        self.writeable_name = writeable_name
        self.language_to_file_map = language_to_file_map
        self.parent = parent
        self.example_number = example_number
        self.read_meta()

        self.json = {}
        self.read()

    def read_meta(self):
        with open(self.language_to_file_map['meta'], 'r') as f:
            content = [l.strip() for l in f.readlines()]

        if content[0] == '---':
            content.pop(0)

        while content and content[0] != '---':
            line = content.pop(0)
            if line:
                key, value = line.split(': ', 1)

                if key == 'name':
                    self.name = value
                elif key == 'nav_order' :
                    self.nav_order = value

        if content and content[0] == '---':
            content.pop(0)
        if content and not content[0]:
            content.pop(0)

        self.text = "\n".join([line + "\n" for line in content])

    def create_output_directories(self):
        # set up the data directory
        if not os.path.exists(self.data_directory_name):
            os.mkdir(self.data_directory_name)

        # set up the representation directory
        if not os.path.exists(self.representations_directory_name):
            os.mkdir(self.representations_directory_name)

    @property
    def data_directory_name(self):
        return os.path.join(self.data_directory, self.writeable_name)

    @property
    def representations_directory_name(self):
        return os.path.join(self.data_directory_name, 'representations')

    def read(self):
        if self.language_to_file_map.get('python'):
            self.read_json()
        
        self.read_representations()

    def read_json(self):
        # override the webbrowser so we don't have to open it
        webbrowser.open_new = lambda _: None

        # load the example
        spec = importlib.util.spec_from_file_location(self.writeable_name, self.language_to_file_map['python'])
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
        if self.json:
            self.representations['json'] = json.dumps(self.json, indent=4, sort_keys=True)

    def write(self, page_directory, data_directory):
        self.page_directory = page_directory
        self.data_directory = data_directory
        self.create_output_directories()
        self.write_data()
        self.write_page()

    def write_data(self):
        # write the json
        if self.json:
            path = os.path.join(self.data_directory_name, 'json.json')
            with open(path, 'w') as f:
                json.dump(self.json, f, indent=4, sort_keys=True)

        # write each representation
        for representation_name, content in self.representations.items():
            path = os.path.join(
                self.representations_directory_name,
                self.writeable_representation(representation_name) + '.json'
            )

            with open(path, 'w') as f:
                json.dump(content, f, indent=4, sort_keys=True)

    @property
    def content(self):
        content = []

        if self.json:
            content.append(self.get_webweb_visualization())

        if self.text:
            content.append(self.text)

        if self.representations and list(self.representations.keys()) != ['meta']:
            content.append(self.get_representations_select())

        if content:
            return "\n".join(content)

    def write_page(self):
        page = util.Page(
            title=self.name,
            writeable_title=self.writeable_name,
            layout='home',
            parent=self.parent,
            content=self.content,
            nav_order=getattr(self, 'nav_order', self.example_number)
        )

        page.write(self.page_directory)

    def get_representations_select(self):
        # display code in a consistent order
        representation_ordering = ['python', 'python (networkx)', 'matlab', 'json']

        ordered_representations = [rep for rep in representation_ordering if self.representations.get(rep)]

        if not ordered_representations:
            return

        select_include = '{{% include code_switcher.html code_options="{options}" switcher_name="example-code-switcher" %}}'.format(
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
        representation_content_path = 'site.data.{parent}.{name}.representations.{representation}'.format(
            parent=self.parent,
            name=self.writeable_name,
            representation=self.writeable_representation(representation),
        )

        language = representation

        if representation == 'python (networkx)':
            language = 'python'

        content = "```{language}\n{{{{{content_path}}}}}\n```".format(
            language=language, 
            content_path=representation_content_path,
        )

        representation_display_classes = [
            "select-code-block",
            "example-code-switcher",
            "{0}-code-block".format(self.writeable_representation(representation)),
        ]

        # make python visible
        if representation == 'python':
            representation_display_classes.append("select-code-block-visible")

        div = "<div class='{0}'></div>".format(" ".join(representation_display_classes))

        return "\n".join([div, content])

    def get_webweb_visualization(self):
        return "{{% include webweb.html webweb_json=site.data.{parent}.{name}.json %}}\n".format(
            parent=self.parent,
            name=self.writeable_name,
        )
