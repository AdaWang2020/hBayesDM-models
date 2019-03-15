# Model Information JSON Files

Greatly contributed by [Jethro Lee][jethro-lee].

[jethro-lee]: https://github.com/dlemfh

## Schema

All the information is stored in `ModelInformation.schema.json` in a JSON schema
format.


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

## Example

***It would be better to provide an example for this. It's a little hard to find
what developers should do to add a model.***

## Validation

Validating against the current Schema file is a good basis to see if you've
written the model JSON file correctly.
To validate the JSON file, you should have [`jsonschema`][jsonschema]; you can
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
