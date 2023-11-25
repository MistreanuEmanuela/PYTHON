import os
import sys

if len(sys.argv) < 2:
    raise Exception("Wrong number of arguments, you should try 'python directory'")

directory = sys.argv[1]
total_size = 0
try:
    for (root, directories, files) in os.walk(directory):
        for fileName in files:
            full_fileName = os.path.join(root, fileName)
            total_size += os.path.getsize(full_fileName)

except FileNotFoundError:
    print("Your path is wrong")
except KeyboardInterrupt:
    print("Operation aborted by the user.")
except PermissionError:
    print(f"Error: Permission denied. Check if you have the necessary permissions to access the files.")
except Exception as e:
    print(f"An error occurred: {e}")


def get_size_new(size):
    dimensions = ['B', 'KB', 'MB', 'GB']
    dim = []
    index = 0

    while size > 1024.0 and index < 3:
        size /= 1024.0
        dim.append(size)
        index += 1
    print(dim)
    return_string = f"{dim[-1]}" + "  " + f"{dimensions[len(dim)]}"
    return return_string.strip()


if total_size:
    print(f"The size of all elements is the directory is : {get_size_new(total_size)}")
else:
    print("The size is 0 ")
