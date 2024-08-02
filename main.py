import os
import base64
import json
from collections import OrderedDict

## Methods
def read_from_file(file_path):
   with open(file_path, 'rb') as file:
     data = file.read()
   return data

def extract_filename(file_path):
    # Extract the filename from the file path
    filename = os.path.basename(file_path)
    return filename

def modify_path(path):
    # Remove trailing slash if it exists
    if path.endswith('/'):
        path = path[:-1]

    # Add leading slash if it doesn't exist
    if not path.startswith('/'):
        path = '/' + path

    return path


#filePath = input("1. Input Nrrd file path: ").replace(" ", "")
#fast = bool(input("2. Fast(bool): "))

filePath = "/Users/happyduck/Desktop/fool.nrrd"
fast = True



# 1. Convert file to base64 format.
file_data = read_from_file(filePath)
encoded_data = base64.b64encode(file_data)
result_str = encoded_data.decode('ascii')

# 2. Make a json format string.
data_dict = OrderedDict()
data_dict["dicomNrrd"] = result_str
data_dict["fast"] = fast

# 3. Save as a json file.


saving_path = input("3. File path you want to save this file: ")

modified_path = modify_path(saving_path)
print(modified_path)

extracted_name = extract_filename(filePath)
newFilePath = f"{modified_path}/{extracted_name}_result.json"
count = 0

while True:
    isExist = os.path.exists(newFilePath)
    if isExist:
        count += 1
        newFilePath = f"{modified_path}/{extracted_name}_result{count}.json"
        continue
    else:
        break

with open(newFilePath, 'w') as f:
    json.dump(data_dict, f)

f.close()

print(f"File saved to {newFilePath}")
