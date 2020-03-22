import os

input_directory_1 = input("Insert the folder you want to move: ")
input_directory_2 = input("Insert the folder that should get the content from the first folder: ")

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


def get_non_duplicate_sub_folder(a, b):
    print('______________FOLDERS THAT YOU HAVE TO MOVE TO THE SECOND ONE______________')
    print([x for x in a if x not in b])


def get_first_folder_matched_sub_folders(a, b):
    return [x for x in a if x not in b]


def get_match_rate(a, b):
    joined_folders = list(sub_folders_0) + list(sub_folders_1)
    print("Total sub-folders from the two main folders: ", len(joined_folders))
    unique_joined_folders = dict.fromkeys(joined_folders)
    print("Total folders without repetition ", len(unique_joined_folders))
    match_folders = get_first_folder_matched_sub_folders(a, b)
    match_rate = len(match_folders) / len(unique_joined_folders)

    print(match_rate)


print(get_non_duplicate_sub_folder(sub_folders_0, sub_folders_1))

get_match_rate(sub_folders_0, sub_folders_1)
