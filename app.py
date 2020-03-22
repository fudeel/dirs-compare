import os

input_directory_1 = "D:\\Fadil\\Loops and Samples"
input_directory_2 = "D:\\Fadil\\Music Production\\Loops and Samples"

folders = [input_directory_1, input_directory_2]


def get_list_0():
    paths = []
    parent_dirs = []

    for root, dirs, files in os.walk(folders[0], topdown=False):
        paths.append(root)
    paths.pop()
    for p in paths:
        parent_dir = p.split(folders[0], 1)[1].split("\\")[1]
        parent_dirs.append(parent_dir)
    parent_dirs = dict.fromkeys(parent_dirs)  # creating unique elements, since dicts accept only unique keys

    return parent_dirs


def get_list_1():
    paths = []
    parent_dirs = []

    for root, dirs, files in os.walk(folders[1], topdown=False):
        paths.append(root)
    paths.pop()
    for p in paths:
        parent_dir = p.split(folders[1], 1)[1].split("\\")[1]
        parent_dirs.append(parent_dir)
    parent_dirs = dict.fromkeys(parent_dirs)  # creating unique elements, since dicts accept only unique keys

    return parent_dirs


sub_folders_0 = get_list_0()
sub_folders_1 = get_list_1()

