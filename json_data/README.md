## Information kept track of by Model Information Schema
Property | Required | Type | Explanation
-|-|-|-
"task_name" | o | String | Name of the task.
"model_name" | o | String | Name of the model.
"model_type" | o | String | Modeling type: `""` or `"single"` or `"multipleB"`.
"data_columns" | o | Array of Strings | Names of the necessary data columns for user data.
"data_for_stan" | x | Array of Strings | Names of the preprocessed data to be passed to Stan.</br> *\* Not really used within code; just here FYI.*
"parameters" | o | Array of Strings | Names of the parameters of this model.
"parameters_info" | o | Array of (len 3) Arrays | Lower bound, plausible value, & upper bound for each parameter.</br> *\* Note that these bounds may differ from the boundary constraints given to the parameters in Stan code.*
"regressors" | x | Array of Strings | Names of the regressors of this model. (Omit if not supported.)
"regressors_info" | x | Array of Integers | Extracted dimension-size for each regressor. (Omit if not supported.)
"postpreds" | o | Array of Strings | Name(s) of the posterior predictions. **Must be specified as array of string(s), e.g. `["y_pred"]`.** Give empty array `[]` if not supported.

## How to validate JSON file(s)
**Requirement:** [`pip install -U jsonschema`](https://github.com/Julian/jsonschema)

To validate a single JSON file:
```sh
jsonschema -i FILE_NAME_HERE ModelInformation.schema.json
```
To validate all JSON files in directory, use following shell script:
```sh
./ValidateAll.sh
```

##### Written by Jethro Lee.
