"""
Application stub
"""

from arjuna import *
from flask import jsonify

# logger = logging.getLogger(__name__)

def initialize():
    # perform heavy stuff here
    return True


def do_stuff():
    # do whatever you need to do
    response = "This is response from Python backend"
    return response

def make_tree(path):
    tree = dict(name=os.path.basename(path), children=[])
    try: lst = os.listdir(path)
    except OSError:
        pass #ignore errors
    else:
        for name in lst:
            fn = os.path.join(path, name)
            if os.path.isdir(fn):
                tree['children'].append(make_tree(fn))
            else:
                tree['children'].append(dict(name=name, type='file'))
    return tree

def traverse_folders(directory):
    import os
    rootdir = directory
    list_files = []

    parent_html = "<ul>"
    subdir_html = ""

    for subdir, dirs, files in os.walk(rootdir):
        if "naveen_env" not in subdir:
            if "report" not in subdir:
                if "pytest_cache" not in subdir:
                    if "pycache" not in subdir:
                        if "guiauto" not in subdir:
                            if "httpauto" not in subdir:
                                if "lib" not in subdir:
                                    if "config" not in subdir:
                                        if "data" not in subdir:
                                            if "dbauto" not in subdir:
                                                if "l10n" not in subdir:
                                                    if "test\\" not in subdir:
                                                        # print(dirs)
                                                        # print(subdir)
                                                        # print(files)
                                                        # print("------------------------")
                                                        subdir_html = "<li>" + subdir
                                                        file_html = "<ul>"
                                                        for file in files:
                                                            if(file.endswith(".py") or file.endswith(".yaml")):
                                                                file_html += "<li data-jstree='{\"type\": \"file\"}'>" + file + "</li>"
                                                                # print(os.path.join(subdir, file))
                                                                # print(dirs)
                                                                # print(subdir)
                                                                # print(file)
                                                                # print("------------------------")
                                                        subdir_html += file_html + "</ul></li>" 
                                                        parent_html += subdir_html
    parent_html += "</ul>"
    return parent_html

# traverse_folders(r"D:\\vscode\\test_arjuna")

# print(make_tree(r"D:\\vscode\\test_arjuna"))


# def traverse_folders(directory):
#     import os
#     rootdir = directory
#     list_files = []

#     parent_dict = dict()

#     for subdir, dirs, files in os.walk(rootdir):
#         if "naveen_env" not in subdir:
#             if "report" not in subdir:
#                 if "pytest_cache" not in subdir:
#                     if "pycache" not in subdir:
#                         if "guiauto" not in subdir:
#                             if "httpauto" not in subdir:
#                                 if "lib" not in subdir:
#                                     if "config" not in subdir:
#                                         # if "test" not in subdir:
#                                             # print(subdir)
                                        
#                                             list_files = []
#                                             for file in files:
#                                                 if(file.endswith(".py") or file.endswith(".yaml")):
#                                                     # print(os.path.join(subdir, file))
#                                                     list_files.append(file)
#                                             parent_dict.update({subdir : list_files})
#     return parent_dict