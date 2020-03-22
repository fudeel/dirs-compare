import os
from tabulate import tabulate

input_directory_1 = "D:\Fadil\Loops and Samples"
input_directory_2 = "D:\Fadil\Music Production\Loops and Samples"

inputs = [input_directory_2]
folders = []


class FolderInfo:
    def __init__(self, root, dirs_num, dirs):
        self.root = root
        self.dirs_num = dirs_num
        self.dirs = dirs

    def get_dirs(self):
        return self.dirs


def get_list():
    paths = []
    parent_dirs = []
    for i in inputs:
        for root, dirs, files in os.walk(i, topdown=False):
            paths.append(root)
        paths.pop()
        for p in paths:
            parent_dir = p.split(i, 1)[1].split("\\")[1]
            parent_dirs.append(parent_dir)
        parent_dirs = list(dict.fromkeys(parent_dirs))  # creating unique elements, since dicts accept only unique keys

        folder = FolderInfo(i, str(len(parent_dirs)), parent_dirs)
        folders.append(folder)


get_list()


for f in folders:
    print(f.get_dirs())
