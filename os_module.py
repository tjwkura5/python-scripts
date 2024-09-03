import os

while True:
    directory = input("Please provide a directory: ")

    if os.path.isdir(directory):
        print("Directory exists")
        break
    else:
        print("Directory does not exist, please provide a valid directory")

dir_num = len([path for path in os.listdir(directory) if os.path.isdir(os.path.join(directory, path))]) - 1

files_num = len([path for path in os.listdir(directory) if os.path.isfile(os.path.join(directory, path))])


print(f'The number of files in this directory is {files_num}')

print(f'The number of directories in this directory is {dir_num}')