import os
import yaml
import shutil

def clean_dir(directory):
    """makes a pages directory if it doesn't exist
    cleans a pages directory if it does"""
    if not os.path.exists(directory):
        os.mkdir(directory)
        return

    for thing in os.listdir(directory):
        thing_path = os.path.join(directory, thing)

        if os.path.isfile(thing_path):
            os.unlink(thing_path)
        elif os.path.isdir(thing_path):
            shutil.rmtree(thing_path)

class Page(object):
    def __init__(self, title, writeable_title='', has_children=False, parent=None, content=None, layout='main_page', permalink=None, nav_order=1, grand_parent=None):
        self.title = title
        self.writeable_title = writeable_title
        self.has_children = has_children
        self.parent = parent
        self.content = content
        self.layout = layout
        self.permalink = permalink
        self.nav_order = nav_order
        self.grand_parent = grand_parent

    @property
    def frontmatter(self):
        content = {
            'title' : self.title,
            'layout' : self.layout,
            'nav_order' : int(self.nav_order),
        }

        if self.parent:
            content['parent'] = self.parent

        if self.grand_parent:
            content['grand_parent'] = self.grand_parent

        if self.permalink:
            content['permalink'] = self.permalink

        if self.has_children:
            content['has_children'] = self.has_children

        return content

    def write(self, output_dir):
        path = os.path.join(output_dir, self.writeable_title + '.md')

        to_write = [
            '---',
            yaml.dump(self.frontmatter, default_flow_style=False),
            '---',
        ]

        if self.content:
            to_write.append("\n" + self.content)

        with open(path, 'w') as f:
            f.write("\n".join(to_write))
