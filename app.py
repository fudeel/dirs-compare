import os


input_directory_1 = "D:\Fadil\Loops and Samples"
input_directory_2 = "D:\Fadil\Music Production\Loops and Samples"

inputs = [input_directory_1, input_directory_2]


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
        print("The folder " + str(i) + "has: " + str(len(parent_dirs)) + " elements")


get_list()
