import sys
import os

if len(sys.argv) < 2:
    raise Exception("Wrong number of arguments, you should try 'python directory'")

files_dir = []
try:
    files_dir = os.listdir(sys.argv[1])
except FileNotFoundError:
    print("Your path is wrong")

for index, file_name in enumerate(files_dir):
    try:
        file_path = os.path.join(sys.argv[1], file_name)
        name1 = file_name.split('.')
        new_path = sys.argv[1]
        new_name = ''
        for i in name1[0]:
            new_name = new_name + i
        new_name += str(index+1)
        new_name += '.'
        new_name += name1[-1]
        print(new_name)
        new_path = os.path.join(new_path, new_name)
        os.rename(file_path, new_path)
    except Exception as e:
        print(f"Unable to rename file '{file_name}': {e}")