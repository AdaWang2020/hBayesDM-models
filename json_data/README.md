## Information kept track of by Model Information Schema:
Property | Required | Explanation
-|-|-
"task_name" | o | Name of the task.
"model_name" | o | Name of the model.
"model_type" | o | Modeling type: `""` or `"single"` or `"multipleB"`.
"data_columns" | o | Names of the necessary data columns for the user data.
"data_for_stan" | x | Names of the preprocessed data to be passed to Stan.</br> *\* Not really used within code; just here FYI.*
"parameters" | o | Names of the parameters of this model.
"parameters_info" | o | Bounds & initial values of the parameters **used in the R/Python codes**.</br> *\* Note that these bounds may differ from the boundary constraints given to the parameters in the Stan code.*
"regressors" | x | Names of the regressors of this model.
"regressors_info" | x | Dimension-sizes of the extracted regressors.
"postpreds" | o | Name(s) of the posterior predictions. **Must be specified as array of string(s), e.g. `["y_pred"]`.**

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
