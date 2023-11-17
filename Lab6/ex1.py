import sys
import os

if len(sys.argv) < 3:
    raise Exception("Wrong number of arguments, you should try 'python directory extension'")

files_sorted = []
try:
    files_dir = os.listdir(sys.argv[1])
    files_sorted = [file for file in files_dir if file.endswith(sys.argv[2])]
    if not files_sorted:
        raise Exception
except FileNotFoundError:
    print("Your path is wrong")
except Exception as e:
    print("Wrong extension or the directory does not contain this type of files")

for file_name in files_sorted:
    try:
        file_path = os.path.join(sys.argv[1], file_name)
        with open(file_path, 'r') as file:
            for line in file:
                print(line.strip())
    except Exception as e:
        print(f"Unable to open file '{file_name}': {e}")