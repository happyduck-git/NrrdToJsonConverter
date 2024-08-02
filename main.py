import base64
import json
from collections import OrderedDict


filePath = input("1. Input Nrrd file path: ").replace(" ", "")
fast = bool(input("2. Fast(bool): "))

def read_from_file(file_path):
   with open(file_path, 'rb') as file:
     data = file.read()
   return data

# 1. Convert file to base64 format.
file_data = read_from_file(filePath)
encoded_data = base64.b64encode(file_data)
result_str = encoded_data.decode('ascii')

# 2. Make a json format string.
data_dict = OrderedDict()
data_dict["dicomNrrd"] = result_str
data_dict["fast"] = fast

# 3. Save as a json file.
with open(".venv/parameter.json", 'w') as f:
    json.dump(data_dict, f)

f.close()