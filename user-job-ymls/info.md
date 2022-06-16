CWL workflow YAML files will automatically be placed here (when `RUN_MODEL.sh` is ran). Contains strings and 
files that machine learning models will use to predict subtypes. The name of the YAML files is 
`<method>-inputs.yml`

Methods have different YAML contents, here is an example for `skgrid-inputs.yml`
```
cancer:
  - BRCA
platform:
  - GEXP
input_data:
  - class: File
    path: ../user-transformed-data/transformed-data.tsv
output_prefix:
  - BRCA_GEXP_skgrid
```
