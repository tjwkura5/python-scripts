import os

while True:
    directory = input("Please provide a directory: ")

    if os.path.isdir(directory):
        print("Directory exists")
        break
    else:
        print("Directory does not exist, please provide a valid directory")

files_num = 0
# set to negative one to not count the existing directory
dir_num = -1

for path in os.listdir(directory):
    # check if current path is a file
    if os.path.isfile(os.path.join(directory, path)):
        files_num += 1

for path in os.listdir(directory):
    # check if current path is a dir
    if os.path.isdir(os.path.join(directory, path)):
        dir_num += 1

print(f' The number of files in this directory is {files_num}')

print(f'The number of directories in this directory is {dir_num}')