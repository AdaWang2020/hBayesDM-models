# Model Information JSON Files

Contributed by [Jethro Lee][jethro-lee].

[jethro-lee]: https://github.com/dlemfh

## JSON Schema

Schema for the Model Information JSON files is stored in
`ModelInformation.schema.json` as a JSON Schema format.

| Property          | Type                | Description
|-------------------|---------------------|----------------------------------|
| `task_name`       | Object              | Informations regarding the task.
| `model_name`      | Object              | Informations regarding the model.
| `model_type`      | Object              | Modeling-type information. Should be one of the following three:</br> - `{"code": "", "desc": "Hierarchical"}`</br> - `{"code": "single", "desc": "Individual"}`</br> - `{"code": "multipleB", "desc": "Multiple-Block Hierarchical"}`
| `notes`           | Array of Strings    | Optional notes about the task/model. Give empty array `[]` if unused.
| `contributors`    | Array of Objects    | Optional specifying of contributors. Give empty array `[]` if unused.
| `data_columns`    | Object              | **Keys**: names of the necessary data columns for user data.</br> - `"subjID"` must always be included.</br> - Also include `"block"`, if modeling-type is "multipleB".</br> **Values**: one-line descriptions about each data column.
| `parameters`      | Object (of Objects) | **Keys**: names of the parameters of this model.</br> **Values**: inner-level Object specifying desc and info for each parameter.
| `regressors`      | Object              | *(Give empty object `{}` if not supported.)*</br> **Keys**: names of the regressors of this model.</br> **Values**: extracted dimension-size for each regressor.
| `postpreds`       | Array of Strings    | Name(s) of posterior predictions. Give empty array `[]` if not supported.
| `additional_args` | Array of Objects    | Specifying of additional arguments, if any. Give empty array `[]` if unused.

*\* Note that all outermost-level properties are required properties. Assign empty values (`[]` or `{}`) to them if unused.*  
*\* Refer below for inner-level Object specifications.*

#### `task_name` & `model_name` Object
| Keys   | Values
|--------|-------------------------------------|
| `code` | *(String)* Code for the task/model.
| `desc` | *(String)* Name of the task/model in title-case.
| `cite` | *(Array of Strings)* Citations for the task/model.

#### `model_type` Object
| Keys     | Values
|----------|----------------------------------------|
| `"code"` | *(String)* Code for the modeling-type.
| `"desc"` | *(String)* Name of the task in title-case.

#### Contributor Object
| Keys     | Values
|----------|-------------------------------|

#### Parameter Object
| Keys     | Values
|----------|-------------------------------|

#### Additional_arg Object
| Property | Type | Description
|----------|------|-------------|

*\* Allowed values for parameter infos (lower bound, plausible value, upper bound):*
- Numbers
- Strings: `"Inf"`, `"-Inf"`, `"exp([0-9.]+)"`
- `null`

## JSON Example

***It would be better to provide an example for this. It's a little hard to find
what developers should do to add a model.***

## JSON Validation

Validating against the current Schema file is a good basis to see if you've
written the model JSON file correctly.
To validate JSON files, you need to have [`jsonschema`][jsonschema] installed; you can
install it with `pip install jsonschema`.

[jsonschema]: https://github.com/Julian/jsonschema

To validate a single JSON file (e.g. `gng_m1.json`):

```sh
$ jsonschema -i gng_m1.json ModelInformation.schema.json
```

To validate all JSON files in directory, use following shell script:

```sh
$ ./ValidateAll.sh
```

## Automated Python Code Generation

Once you've (correctly) written the JSON file for a new model, it's possible to
automatically generate the corresponding python code for the new model,
using the python script `WritePython.py`:

```
$ ./WritePython.py -h
usage: WritePython.py [-h] [-v] json_file

positional arguments:
  json_file      JSON file of the model to generate corresponding python code

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  print output to stdout instead of writing to file
```

E.g. (generate `_gng_m1.py` from `gng_m1.json`):

```sh
$ ./WritePython.py gng_m1.json
Created file: _gng_m1.py
```
