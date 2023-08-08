# Files

There will be two results files.

1. The sample subtype prediction file will have the suffix "cloudforest_preds.tsv" (full name
`<cancer>_<platform>_cloudforest_preds.tsv`). Columns
1-3 indicate the sampleID, predicted subtype, and actual subtype.  Note
the actual subtype column will be NA if the subtypes aren't provided by
the user (this will be most user cases).

2. The model vote file will have the suffix "cloudforest_votes.vo" (full name `<cancer>_<platform>_cloudforest_votes.vo`) and contains the categorical vote totals.  

An input file with the suffix `.sf` is automatically fed into the machine learning model. This is the associated file for the top CloudForest model.

# Model Notations

The following data platforms can be specified for CloudForest: `All` `CNVR` `GEXP` `METH` `MIR` `MUTA` `OVERALL`. Where
`All` models must use all available data types (CNVR, GEXP, METH, MIR, and MUT).  `OVERALL` is the best model
for the cohort (this can be a model that uses a single platform, several platforms, or all platforms; it simply returns the model that had the highest performance).  

CloudForest does not include `MIR` models for `KIRCKICH`, `LGGGBM` or `LIHCCHOL`.
