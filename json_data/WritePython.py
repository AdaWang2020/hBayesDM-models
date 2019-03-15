#!/usr/bin/env python3
"""
Written by Jethro Lee.
"""
import sys
import json
import argparse
from collections import OrderedDict
from pathlib import Path


def main(json_file, verbose):
    # Make a Path object for the given filename
    path_fn = Path(json_file)

    # Check if the file exists
    if not path_fn.exists():
        print('FileNotFound: Please specify existing json_file as argument.')
        sys.exit(1)

    # Load json_file
    with open(path_fn, 'r') as f:
        model_info = json.load(f, object_pairs_hook=OrderedDict)

    # Model full name (Snakecase)
    full_name = path_fn.name.replace('.json', '')

    # Model class name (Pascalcase)
    class_name = full_name.title().replace('_', '')

    # Read template for docstring
    with open('PY_DOCSTRING_TEMPLATE.txt', 'r') as f:
        docstring_template = f.read().format()

    # Read template for model python code
    with open('PY_CODE_TEMPLATE.txt', 'r') as f:
        code_template = f.read().format(
            task_name=model_info['task_name'],
            model=full_name,
            class_name=class_name,
            docstring_template=docstring_template)

    if verbose:
        # Just print the code string into stdin
        print(code_template)
    else:
        # Write model python code
        with open('_' + full_name + '.py', 'w') as f:
            f.write(code_template)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-v', '--verbose',
        help='Whether to print the output instead of writing a file',
        action='store_true')
    parser.add_argument(
        'json_file',
        help=('A JSON file about a model to generate a corresponding '
              'Python code'),
        type=str)

    args = parser.parse_args()

    main(args.json_file, args.verbose)
