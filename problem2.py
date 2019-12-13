import os

path = "/Users/cfleury/Documents/testdir"
broken_path = '/folder/dir'
file_name = "/Users/cfleury/Documents/testdir/t1.c"

os.chdir(path)

checked_folders = []

file_list = []


def find_files(dir_path):
    if os.path.exists(dir_path) and not os.path.isfile(dir_path):
        for dir_file in os.listdir(dir_path):
            filename = os.path.basename(dir_file)
            if os.path.isdir(dir_path + '/' + dir_file):
                #recursively finds files in subdirectories
                find_files(dir_path + '/' + filename)
            elif os.path.isfile(dir_path + '/' + dir_file):
                if filename.endswith('.c'):
                    file_list.append(dir_path + '/' + filename)

        return file_list

    return -1


print(find_files(path)) #['b.c', 't1.c', 'a.c', 'a.c']

#edge case 1
print(find_files(broken_path)) # returns -1

#edge case 2
print(find_files(file_name)) # returns -1



