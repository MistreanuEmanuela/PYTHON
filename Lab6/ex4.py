import sys
import os

if len(sys.argv) < 2:
    raise Exception("Wrong number of arguments, you should try 'python directory'")

directory = sys.argv[1]
dictionary_extension = {}
files_dir = []
try:
    for (root, directories, files) in os.walk(directory):
        for fileName in files:
            file_name = fileName.split('.')
            if file_name[1] in dictionary_extension.keys():
                dictionary_extension[file_name[1]] += 1
            else:
                dictionary_extension[file_name[1]] = 1
        if not files:
            raise Exception
except FileNotFoundError:
    print("Your path is wrong")
except PermissionError:
    print(f"Error: Permission denied. Check if you have the necessary permissions to access the files.")
except Exception:
    print("The directory is empty")

for key in dictionary_extension.keys():
    print(f"Number of files with extension {key} are: {dictionary_extension[key]}")