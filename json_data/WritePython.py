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
            contributors=format_list(
                model_info['contributors'], 'name', 'email',
                f='.. codeauthor:: {} <{}>', sep='\n    '),
            data_columns=format_dict_keys(
                model_info['data_columns'], f='"{}"', sep=', '),
            data_columns_len=len(model_info['data_columns']),
            data_columns_details=format_dict_items(
                model_info['data_columns'], f='- "{}": {}', sep='\n    '),
            parameters=format_parameters(model_info['parameters']),
            model_regressor_parameter=format_model_regressor_parameter(
                model_info['regressors']),
            model_regressor_return=format_model_regressor_return(
                model_info['regressors']),
            postpreds=format_postpreds(model_info['postpreds']),
            additional_args=format_additional_args(
                model_info['additional_args']),
        )

    # Read template for model python code
    with open('PY_CODE_TEMPLATE.txt', 'r') as f:
        code_template = f.read().format(
            docstring_template=docstring_template,
            model_function=model_function,
            class_name=class_name,
            task_name=model_info['task_name']['code'],
            model_name=model_info['model_name']['code'],
            model_type=model_info['model_type']['code'],
            data_columns=format_dict_keys(
                model_info['data_columns'],
                f="'{}'", sep=',\n                '),
        )

    if verbose:
        # Print code string to stdout
        print(code_template)
    else:
        # Write model python code
        code_fn = '_' + model_function + '.py'
        with open(code_fn, 'w') as f:
            f.write('"""\nGenerated by template. Do not edit by hand.\n"""\n')
            f.write(code_template)
        print('Created file: ' + code_fn)


def format_list(data: List, *keys: str, f: str, sep: str):
    return sep.join([f.format(*(d[k] for k in keys)) for d in data])


def format_dict_keys(data: OrderedDict, f: str, sep: str) -> str:
    return sep.join([f.format(k) for k in data.keys()])


def format_dict_items(data: OrderedDict, f: str, sep: str) -> str:
    return sep.join([f.format(k, v) for k, v in data.items()])


def format_parameters(parameters: OrderedDict) -> str:
    return ', '.join(
        ['"{}" ({})'.format(k, v['desc']) for k, v in parameters.items()])


def format_model_regressor_parameter(regressors: OrderedDict) -> str:
    if regressors:
        return 'For this model they are: ' + format_dict_keys(
            regressors, f='"{}"', sep=', ')
    else:
        return 'Currently not available for this model'


def format_model_regressor_return(regressors: OrderedDict) -> str:
    if regressors:
        return (
            '- ``model_regressor``: '
            + 'Dict holding the extracted model-based regressors.')
    else:
        return ''


def format_postpreds(postpreds: List) -> str:
    if not postpreds:
        return '**(Currently not available.) **'
    else:
        return ''


def format_additional_args(additional_args: List) -> str:
    if additional_args:
        return (
            'For this model, it\'s possible to set the following **model-'
            + 'specific argument** to a value that you may prefer.\n\n        '
            + format_list(
                additional_args, 'code', 'desc',
                f='- ``{}``: {}', sep='\n        '))
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
