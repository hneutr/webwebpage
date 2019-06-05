import yaml

from pathlib import Path


def update(webweb_dir, changelog_file):
    changelog_path = Path(webweb_dir).joinpath('changelog.md')

    frontmatter = {
        'title': 'changelog',
        'nav_order': 6,
        'layout': 'main_page',
        'permalink': '/changelog/',
    }

    to_write = "\n".join([
        '---',
        yaml.dump(frontmatter, default_flow_style=False),
        '---',
        changelog_path.read_text(),
    ])

    changelog_file.touch()
    changelog_file.write_text(to_write)
