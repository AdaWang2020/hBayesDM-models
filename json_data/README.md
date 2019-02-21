### Information currently kept track of by Model Information Schema:
Property | Required | Explanation
-|-|-
"model" | o | Full name of the model.
"data_columns" | o | Names of the necessary data columns for the user data.
"data_for_stan" | o | Names of the preprocessed data to be passed to Stan.
"parameters" | o | Names of the parameters of this model.
"parameters_info" | o | Bounds & initial values of the parameters **used in the R/Python codes**.</br> *\* Note that these bounds may differ from the boundary constraints given to the parameters in the Stan code.*
"regressors" | x | Names of the regressors of this model.
"regressors_info" | x | Dimension-sizes of the extracted regressors.
"postpreds" | o | Name(s) of the posterior predictions. **Must be specified as array of string(s).**

#### Written by Jethro Lee.
