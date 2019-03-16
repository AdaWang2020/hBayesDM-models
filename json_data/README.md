# Model Information JSON Files

Contributed by [Jethro Lee][jethro-lee].

[jethro-lee]: https://github.com/dlemfh

## JSON Schema

Schema for the Model Information JSON files is stored in
`ModelInformation.schema.json` as a JSON Schema format.

| Property       | Required | Type             | Explanation
|----------------|----------|------------------|-------------------------------|
| `task_name`    | o        | String           | Name of the task.
| `model_name`   | o        | String           | Name of the model.
| `model_type`   | o        | String           | Modeling type: `""` or `"single"` or `"multipleB"`.
| `data_columns` | o        | Array of Strings | Names of the necessary data columns for user data.</br> - `"subjID"` must always be included.</br> - Also include `"block"` if "model_type" is `"multipleB"`.
| `parameters`   | o        | Object(dict)     | **Keys**: names of the parameters of this model.</br> **Values**: (len 3 array) lower bound, plausible value, & upper bound for each parameter.</br> *\* See below for allowed values.*
| `regressors`   |          | Object(dict)     | *(Omit if regressors are not supported.)*</br> **Keys**: names of the regressors of this model.</br> **Values**: extracted dimension-size for each regressor.
| `postpreds`    | o        | Array of Strings | Name(s) of the posterior predictions. **Must be specified as array of string(s)**, e.g. `["y_pred"]`. Give empty array `[]` if not supported.

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
jsonschema -i gng_m1.json ModelInformation.schema.json
```

To validate all JSON files in directory, use following shell script:

```sh
./ValidateAll.sh
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

Example (to generate `_gng_m1.py` from `gng_m1.json`):

```sh
./WritePython.py gng_m1.json
```
