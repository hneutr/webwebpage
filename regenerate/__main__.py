# this script recreates from scratch the documentation
import argparse
import os
import shutil
import subprocess
from pathlib import Path

from examplify import examplify
import changelog
import util

WEBWEB_URL = "https://github.com/dblarremore/webweb.git"
WEBWEB_DIR = os.path.join(os.getcwd(), 'webweb')
WEBWEB_CODE = os.path.join(WEBWEB_DIR, 'webweb', 'webweb.py')

JEKYLL_ASSETS_DIR = os.path.join(os.getcwd(), 'assets')
WEBWEB_ASSETS_DIR = os.path.join(os.getcwd(), 'webweb', 'client')

EXAMPLES_INPUT_DIR = os.path.join(os.getcwd(), 'webweb', 'examples')
EXAMPLES_DATA_OUTPUT_DIR = os.path.join(os.getcwd(), '_data', 'examples')
EXAMPLES_PAGES_OUTPUT_DIR = os.path.join(os.getcwd(), 'docs', 'examples')

DOCUMENTATION_PAGES_OUTPUT_DIR = os.path.join(os.getcwd(), 'docs', 'documentation')

DISPLAY_INPUT_DIR = os.path.join(os.getcwd(), 'webweb', 'docs', 'display')

DISPLAY_DATA_OUTPUT_DIR = os.path.join(os.getcwd(), '_data', 'documentation', 'display')
DISPLAY_PAGES_OUTPUT_DIR = os.path.join(os.getcwd(), 'docs', 'documentation', 'display')

PYDOC_PAGES_OUTPUT_DIR = os.path.join(DOCUMENTATION_PAGES_OUTPUT_DIR, 'python')

CHANGELOG_FILE = Path.cwd().joinpath('docs', 'changelog.md')

def refresh_webweb():
    if os.path.isdir(WEBWEB_DIR):
        shutil.rmtree(WEBWEB_DIR)

    clone_webweb()
    copy_webweb_client_to_site()


def clone_webweb():
    process = subprocess.Popen('git clone {0}'.format(WEBWEB_URL), shell=True)
    process.wait()


def copy_webweb_client_to_site():
    """copies the webweb assets to a jekyll-friendly location"""
    for content_type in ['css', 'js']:
        assets_directory = os.path.join(JEKYLL_ASSETS_DIR, content_type, 'webweb')

        util.clean_dir(assets_directory)

        webweb_content_type_directory = os.path.join(WEBWEB_ASSETS_DIR, content_type)

        for file_name in os.listdir(webweb_content_type_directory):
            full_path = os.path.join(webweb_content_type_directory, file_name)

            if os.path.isfile(full_path):
                destination = os.path.join(assets_directory, file_name)
                shutil.copyfile(full_path, destination)


def docutize(output_dir):
    util.clean_dir(output_dir)

    title = 'documentation'

    util.Index(
        title=title,
        writeable_title=title,
        nav_order=4,
        layout='main_page',
        has_children=True,
        content="full documentation for webweb's parameters and interfaces"
    ).write(output_dir)

    examplify(
        input_dir=DISPLAY_INPUT_DIR,
        data_output_dir=DISPLAY_DATA_OUTPUT_DIR,
        pages_output_dir=DISPLAY_PAGES_OUTPUT_DIR,
        nav_order=1,
        container='display',
        parent_container='documentation'
    )

    py_output_dir = os.path.join(output_dir, 'python')
    pydocutize(py_output_dir, 'documentation', 2)


def pydocutize(output_dir, parent, nav_order):
    functions_mapping = {
        'Web': {
            'display_name': 'webweb.Web',
            'functions': [
                '__init__',
                'show',
                'save',
            ],
        },
        'Network': {
            'display_name': 'webweb.Network',
            'functions': [
                '__init__',
                'add_layer',
            ],
        }
    }

    util.clean_dir(output_dir)
    import pydoc
    import inspect
    webweb_module = util.get_module('webweb', WEBWEB_CODE)

    container = 'python'

    with open('python_documentation.md', 'r') as f:
        index_content = f.read()

    util.Index(
        title=container,
        writeable_title=container,
        nav_order=2,
        layout='main_page',
        has_children=True,
        parent=parent,
        content=index_content,
    ).write(output_dir)

    counter = 1
    for object_name in functions_mapping.keys():
        _object = getattr(webweb_module, object_name)

        object_display_name = functions_mapping[object_name]['display_name']

        for function_name in functions_mapping[object_name]['functions']:
            function_object = getattr(_object, function_name)
            function_signature = inspect.signature(function_object)

            # we want to exclude `self`
            parameters_list = []
            for parameter, parameter_string in function_signature.parameters.items():
                if parameter != 'self':
                    parameters_list.append(str(parameter_string))

            signature_string = "(" + ", ".join(parameters_list) + ")"

            function_doc = pydoc.getdoc(function_object)
            qualified_function_name = object_display_name
            writeable_function_name = object_display_name
            if function_name == '__init__':
                function_doc = pydoc.getdoc(_object) + "\n\n" + function_doc
            else:
                qualified_function_name += '.' + function_name
                writeable_function_name += '_' + function_name

            content = "```python\n{name}{signature}\n````\n\n{doc}".format(
                name=qualified_function_name,
                signature=signature_string,
                doc=function_doc,
            )

            util.Page(
                title=qualified_function_name,
                writeable_title=writeable_function_name,
                nav_order=counter,
                layout='main_page',
                parent=container,
                grand_parent=parent,
                content=content,
            ).write(output_dir)

            counter += 1



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    refresh_webweb()
    # examplify(
    #     input_dir=EXAMPLES_INPUT_DIR,
    #     data_output_dir=EXAMPLES_DATA_OUTPUT_DIR,
    #     pages_output_dir=EXAMPLES_PAGES_OUTPUT_DIR,
    #     nav_order=3,
    #     container='examples',
    # )
    # docutize(DOCUMENTATION_PAGES_OUTPUT_DIR)
    changelog.update(webweb_dir=WEBWEB_DIR, changelog_file=CHANGELOG_FILE)
