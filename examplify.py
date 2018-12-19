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

DEFAULT_INPUT_DIR = os.path.join(os.getcwd(), 'webweb', 'examples')
DEFAULT_DATA_OUTPUT_DIR = os.path.join(os.getcwd(), '_data', 'examples')
DEFAULT_PAGES_OUTPUT_DIR = os.path.join(os.getcwd(), 'docs', 'examples')

def get_example_language_code(language_file_map):
    code = {}

    for lang_name, lang_file_path in language_file_map.items():
        with open(lang_file_path, 'r') as f:
            lang_code = f.readlines()

        # remove trailing newline
        lang_code[-1] = lang_code[-1].rstrip()

        code[lang_name] = lang_code

    return code

def get_example_data(name, language_file_map):

    # override the webbrowser so we don't have to open it
    webbrowser.open_new = lambda _: None

    # load the example
    spec = importlib.util.spec_from_file_location(name, language_file_map['python'])
    example_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(example_module)

    # we need two kinds of json:
    # 1. raw json (for supplying to the webweb visualization of the example)
    # 2. pretty json (for displaying in case someone is curious)
    raw_json = json.loads(example_module.web.json)

    pretty_json = []
    pretty_json_list = json.dumps(raw_json, indent=4, sort_keys=True).split("\n")
    for line in pretty_json_list[:-1]:
        pretty_json.append(line + "\n")

    pretty_json.append(pretty_json_list[-1])

    return {
        'code' : get_example_language_code(language_file_map),
        'json' : {
            'raw' : raw_json,
            'pretty' : pretty_json,
        }
    }

def write_example_data(output_dir, data):
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    for data_type, data_vals in data.items():
        data_type_output_dir = os.path.join(output_dir, data_type)

        if not os.path.exists(data_type_output_dir):
            os.mkdir(data_type_output_dir)

        for data_val_key, data_val_content in data_vals.items():
            fn = os.path.join(data_type_output_dir, data_val_key + '.json')

            with open(fn, 'w') as f:
                json.dump(data_val_content, f, indent=4, sort_keys=True)

def get_example_page(name, language_file_map, example_number):
    frontmatter = {
        'title' : name.replace('_', ' '),
        'layout' : 'home',
        'parent' : 'examples',
        'nav_order' : example_number,
    }

    # we always have python code, so be consistent and show it first
    # and show json last
    forced_order = [
        ('python', 'site.data.examples.{}.code.python'.format(name)),
        ('matlab', 'site.data.examples.{}.code.matlab'.format(name)),
        ('json', 'site.data.examples.{}.json.pretty'.format(name)),
    ]

    language_file_map['json'] = 1

    code_select_options_string = "\n".join([
        "{%- capture code_options -%}",
        "---".join([l for l, _ in forced_order if language_file_map.get(l)]),
        "{%- endcapture -%}",
    ])

    code_select_include_string = "{% include code_switcher.html code_options=code_options %}"

    code_blocks = []
    for language, language_data_path in forced_order:
        if not language_file_map.get(language):
            continue

        code_display_string = "```{0}\n{{{{{1}}}}}\n```".format(language, language_data_path)

        classes = ["select-code-block"]

        # python will be visible
        if language == 'python':
            classes.append("select-code-block-visible")

        class_string = " ".join(classes)

        id_string = "{}-code-block".format(language)

        code_div_string = "<div id='{0}' class='{1}'></div>".format(id_string, class_string)

        code_block = "\n".join([code_div_string, code_display_string])

        code_blocks.append(code_block)

    code_blocks_string = "\n".join(code_blocks)

    content = "\n".join([
        code_select_options_string,
        code_select_include_string,
        code_blocks_string
    ])

    return {
        'content' : content,
        'frontmatter' : frontmatter,
    }


def write_example_page(output_file, page_data):
    with open(output_file, 'w') as f:
        f.write('---\n')
        f.write(yaml.dump(page_data['frontmatter'], default_flow_style=False))
        f.write('\n---\n\n')

        f.write(page_data['content'])

def make_examples(input_dir, data_output_dir, pages_output_dir):
    examples_map = get_examples_map(input_dir)

    for number, (name, language_file_map) in enumerate(sorted(examples_map.items())):
        # data
        example_data_output_dir = os.path.join(data_output_dir, name)
        example_data = get_example_data(name, language_file_map)
        write_example_data(example_data_output_dir, example_data)

        # page
        example_page_output_file = os.path.join(pages_output_dir, name + '.md')
        example_page = get_example_page(name, language_file_map, number + 1)
        write_example_page(example_page_output_file, example_page)

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
            'python' : 'python/simple.py'
            'matlab' : 'matlabl/simple.m'
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
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', '-i', default=DEFAULT_INPUT_DIR, help="the directory to generate examples from")
    parser.add_argument('--data_output_dir', '-d', default=DEFAULT_DATA_OUTPUT_DIR, help="the directory to output example data to")
    parser.add_argument('--pages_output_dir', '-p', default=DEFAULT_PAGES_OUTPUT_DIR, help="the directory to output example pages to")

    args = parser.parse_args()

    prepare_data_output_dir(args.data_output_dir)
    prepare_pages_output_dir(args.pages_output_dir)

    make_examples(args.input_dir, args.data_output_dir, args.pages_output_dir)
