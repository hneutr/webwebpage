# this script recreates from scratch the documentation
from examplify import examplify
from docutize import docutize
import argparse
import os
import shutil
import subprocess

import util

WEBWEB_URL = "https://github.com/dblarremore/webweb.git"
WEBWEB_DIR = os.path.join(os.getcwd(), 'webweb')

JEKYLL_ASSETS_DIR = os.path.join(os.getcwd(), 'assets')
WEBWEB_ASSETS_DIR = os.path.join(os.getcwd(), 'webweb', 'client')

EXAMPLES_INPUT_DIR = os.path.join(os.getcwd(), 'webweb', 'examples')
EXAMPLES_DATA_OUTPUT_DIR = os.path.join(os.getcwd(), '_data', 'examples')
EXAMPLES_PAGES_OUTPUT_DIR = os.path.join(os.getcwd(), 'docs', 'examples')

DISPLAY_INPUT_DIR = os.path.join(os.getcwd(), 'webweb', 'docs', 'display')
DISPLAY_DATA_OUTPUT_DIR = os.path.join(os.getcwd(), '_data', 'display')
DISPLAY_PAGES_OUTPUT_DIR = os.path.join(os.getcwd(), 'docs', 'display')

# DONE:
# 1. get the github repo
#     - update it if there
# 2. set up the webweb code
# 3. set up the directories
#     - clean them if they exist
#     - create them if they don't
# 4. create the examples

# 5. create the documentation

def refresh_webweb():
    if os.path.isdir(WEBWEB_DIR):
        shutil.rmtree(WEBWEB_DIR)

    clone_webweb()
    copy_webweb_client_to_site()

def clone_webweb():
    # clone the repo
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

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    refresh_webweb()
    examplify(
        input_dir=EXAMPLES_INPUT_DIR,
        data_output_dir=EXAMPLES_DATA_OUTPUT_DIR,
        pages_output_dir=EXAMPLES_PAGES_OUTPUT_DIR,
        nav_order=3,
        collection_name='examples',
    )
    examplify(
        input_dir=DISPLAY_INPUT_DIR,
        data_output_dir=DISPLAY_DATA_OUTPUT_DIR,
        pages_output_dir=DISPLAY_PAGES_OUTPUT_DIR,
        nav_order=4,
        collection_name='display',
    )
    # docutize(DOCUMENTATION_INPUT_DIR, DOCUMENTATION_DATA_OUTPUT_DIR, DOCUMENTATION_PAGES_OUTPUT_DIR)
