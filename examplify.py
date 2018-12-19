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

    content = []
    for language_name in language_file_map.keys():
        line = "```{0}\n{{{{site.data.examples.{1}.code.{0}}}}}\n```".format(language_name, name)
        content.append(line)

    content.append("```json\n{{{{site.data.examples.{0}.json.pretty}}}}\n```".format(name))

    return {
        'content' : "\n".join(content),
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

    if not os.path.exists(args.data_output_dir):
        os.mkdir(args.data_output_dir)

    if not os.path.exists(args.pages_output_dir):
        os.mkdir(args.pages_output_dir)

    make_examples(args.input_dir, args.data_output_dir, args.pages_output_dir)
