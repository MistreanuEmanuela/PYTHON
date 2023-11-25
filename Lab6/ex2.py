import sys
import os

if len(sys.argv) < 2:
    raise Exception("Wrong number of arguments, you should try 'python directory'")

files_dir = []
try:
    files_dir = [f for f in os.listdir(sys.argv[1]) if os.path.isfile(os.path.join(sys.argv[1], f))]
except FileNotFoundError:
    print("Your path is wrong")

for index, file_name in enumerate(files_dir):
    try:
        file_path = os.path.join(sys.argv[1], file_name)
        name, extension = os.path.splitext(file_name)
        new_name = f"{name}{index + 1 }{extension}"
        new_path = os.path.join(sys.argv[1], new_name)
        os.rename(file_path, new_path)
        print(f"Renamed: {file_name} -> {new_name}")
    except Exception as e:
        print(f"Unable to rename file '{file_name}': {e}")