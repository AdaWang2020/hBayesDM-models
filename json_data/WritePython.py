#! python3
# Written by Jethro Lee.
import sys
import json
from collections import OrderedDict

help_message = '''
Usage:
    ./WritePython.py [json_file]    # Write model python code for [json_file]
'''

# Check sys argument
if len(sys.argv) != 2:
    print(help_message)
    sys.exit()

# Load json_file
try:
    with open(sys.argv[1], 'r') as f:
        model_info = json.load(f, object_pairs_hook=OrderedDict)
except FileNotFoundError:
    print(help_message)
    print('FileNotFound: Please specify existing json_file as argument.')
    sys.exit()

# Model full name (snake-case)
model = sys.argv[1][:-5]

# Model class name (pascal-case)
class_name = model.title().replace('_', '')

# Read template for docstring
with open('PY_DOCSTRING_TEMPLATE.txt', 'r') as f:
    docstring_template = f.read().format()

# Read template for model python code
with open('PY_CODE_TEMPLATE.txt', 'r') as f:
    code_template = f.read().format(
        task_name=model_info['task_name'],
        model=model,
        class_name=class_name,
        docstring_template=docstring_template)

# Write model python code
with open('_' + model + '.py', 'w') as f:
    f.write(code_template)
