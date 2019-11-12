import os
from pathlib import Path, PurePosixPath


def sitemap_tree(path):
    tree = dict(name=PurePosixPath(path).name, children=[])
    try:
        mylist = os.listdir(path)
    except OSError:
        pass
    else:
        for name in mylist:
            fn = os.path.join(path, name)
            if os.path.isdir(fn):
                tree['children'].append(sitemap_tree(fn))
            else:
                np = os.path.join(name)
                if np.startswith('/'):
                    np = np[1:]
                tree['children'].append(dict(name=np))
    return tree
