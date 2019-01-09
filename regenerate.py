# this script recreates from scratch the documentation
import os
import shutil
import subprocess

WEBWEB_URL = "https://github.com/hneutr/webweb.git"

JEKYLL_ASSETS_DIRECTORY = os.path.join(os.getcwd(), 'assets')
WEBWEB_ASSETS_DIRECTORY = os.path.join(os.getcwd(), 'webweb', 'client')

# DONE:
# 1. get the github repo
#     - update it if there
# 2. set up the webweb code

# 3. set up the directories
#     - clean them if they exist
#     - create them if they don't
# 4. create the examples
# 5. create the documentation

def get_newest_webweb():
    webweb_dir = os.path.join(os.getcwd(), 'webweb')

    # remove the repo if it exists
    if os.path.isdir(webweb_dir):
        shutil.rmtree(webweb_dir)

    # clone the repo
    process = subprocess.Popen('git clone {0}'.format(WEBWEB_URL), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    process.wait()

def get_jekyll_webweb_asset_path(content_type):
    return os.path.join(JEKYLL_ASSETS_DIRECTORY, content_type, 'webweb')

def clean_webweb_assets(content_type):
    directory = get_jekyll_webweb_asset_path(content_type)

    if os.path.isdir(directory):
        shutil.rmtree(directory)

    os.mkdir(directory)

def copy_webweb_assets():
    """copies the webweb assets to a jekyll-friendly location"""
    for content_type in ['css', 'js']:
        # clean/make the directory
        clean_webweb_assets(content_type)

        webweb_content_type_directory = os.path.join(WEBWEB_ASSETS_DIRECTORY, content_type)

        for file_name in os.listdir(webweb_content_type_directory):
            full_path = os.path.join(webweb_content_type_directory, file_name)

            if os.path.isfile(full_path):
                destination = os.path.join(get_jekyll_webweb_asset_path(content_type), file_name)
                shutil.copyfile(full_path, destination)

if __name__ == '__main__':
    print("RUNNING FROM HUNTER's REPO")
    get_newest_webweb()
    copy_webweb_assets()
