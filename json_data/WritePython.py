#!/usr/bin/env python3
"""
Written by Jethro Lee.
"""
import sys
import argparse
import json
from pathlib import Path
from typing import List
from collections import OrderedDict


def main(json_file, verbose):
    # Make Path object for given filename
    path_fn = Path(json_file)

    # Check if file exists
    if not path_fn.exists():
        print('FileNotFound: Please specify existing json_file as argument.')
        sys.exit(1)

    # Load json_file
    with open(path_fn, 'r') as f:
        model_info = json.load(f, object_pairs_hook=OrderedDict)

    # Model full name (Snake-case)
    model_function = path_fn.name.replace('.json', '')

    # Model class name (Pascal-case)
    class_name = model_function.title().replace('_', '')

    # Read template for docstring
    with open('PY_DOCSTRING_TEMPLATE.txt', 'r') as f:
        docstring_template = f.read().format(
            model_function=model_function,
            task_name=model_info['task_name']['desc'],
            task_cite=model_info['task_name']['cite'],
            model_name=model_info['model_name']['desc'],
            model_cite=model_info['model_name']['cite'],
            model_type=model_info['model_type']['desc'],
            contributors=format_contributors(model_info['contributors']),
            data_columns=format_data_columns(model_info['data_columns']),
            data_columns_len=len(model_info['data_columns']),
            data_columns_details=format_data_columns_details(model_info['data_columns']),
            parameters=format_parameters(model_info['parameters']),
            model_regressor_parameter=format_model_regressor_parameter(model_info['regressors']),
            model_regressor_return=format_model_regressor_return(model_info['regressors']),
            postpreds_not_available=format_postpreds_not_available(model_info['postpreds']),
            additional_args=format_additional_args(model_info['additional_args']),
        )

    # Read template for model python code
    with open('PY_CODE_TEMPLATE.txt', 'r') as f:
        code_template = f.read().format(
            task_name=model_info['task_name']['code'],
            model_function=model_function,
            class_name=class_name,
            docstring_template=docstring_template,
        )

    if verbose:
        # Print code string to stdout
        print(code_template)
    else:
        # Write model python code
        code_fn = '_' + model_function + '.py'
        with open(code_fn, 'w') as f:
            f.write(code_template)
        print('Created file: ' + code_fn)


def format_contributors(contributors: List) -> str:
    return '\n    '.join([
        '.. codeauthor:: {name} <{email}>'.format(
            name=contributor['name'],
            email=contributor['email'],
        ) for contributor in contributors
    ])


def format_data_columns(data_columns: OrderedDict) -> str:
    return ', '.join([
        '"{code}"'.format(
            code=key,
        ) for key in data_columns.keys()
    ])


def format_data_columns_details(data_columns: OrderedDict) -> str:
    return '\n    '.join([
        '- "{code}": {desc}'.format(
            code=key,
            desc=value,
        ) for key, value in data_columns.items()
    ])


def format_parameters(parameters: OrderedDict) -> str:
    return ', '.join([
        '"{code}" ({desc})'.format(
            code=key,
            desc=value['desc'],
        ) for key, value in parameters.items()
    ])


def format_model_regressor_parameter(regressors: OrderedDict) -> str:
    if regressors:
        return 'For this model they are: ' + ', '.join([
            '"{code}"'.format(
                code=key,
            ) for key in regressors.keys()
        ])
    else:
        return 'Currently not available for this model'


def format_model_regressor_return(regressors: OrderedDict) -> str:
    if regressors:
        return '- ``model_regressor``: Dict holding the extracted model-based regressors.'
    else:
        return ''


def format_postpreds_not_available(postpreds: List) -> str:
    if not postpreds:
        return '**(Currently not available.)**'
    else:
        return ''


def format_additional_args(additional_args: List) -> str:
    if additional_args:
        return (
            'For this model, it\'s possible to set the following **model-'
            + 'specific argument** to a value that you may prefer.\n\n        '
            + '\n        '.join([
                '- ``{code}``: {desc}'.format(
                    code=additional_arg['code'],
                    desc=additional_arg['desc'],
                ) for additional_arg in additional_args
            ])
        )
    else:
        return 'Not used for this model.'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-v', '--verbose',
        help='print output to stdout instead of writing to file',
        action='store_true')
    parser.add_argument(
        'json_file',
        help='JSON file of the model to generate corresponding python code',
        type=str)

    args = parser.parse_args()

    main(args.json_file, args.verbose)
