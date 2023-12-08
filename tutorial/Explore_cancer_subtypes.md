# Explore Cancer Subtypes
### Understanding Subtype Abbreviations
We have used cancer subtypes abbreviations for classifiers, this means that the output prediction file contains these abbreviations. There is a quick and easy way to pull the full subtype name.

Let's look at the breast invasive carcinoma subtypes `BRCA`. In python:
```
import json
with open('tools/cancer2name.json', 'r') as fh:
    for line in fh:
        cancer2name = json.loads(line)
```

This loads a python dictionary where the keys are the cancer cohort and the values are a second dictionary where the keys are the subtype abbreviation and the values are the subtype name

If we want to look up the name of the first breast invasive carcinoma subtype (abbreviation `BRCA_1`):
```
cancer2name['BRCA']['BRCA_1']
```
> 'LumA'

### Other Uses
If we want to survey all the subtype names of a cancer cohort we can extract the nested python dictionary by:
```
cancer2name['BRCA']
```
> {'BRCA_1': 'LumA', 'BRCA_2': 'LumB', 'BRCA_3': 'Basal', 'BRCA_4': 'Her2'}

### General Navigation
To view all cancer cohort options:
```
cancer2name.keys()
```
> dict_keys(['ACC', 'BLCA', 'BRCA', 'CESC', 'COADREAD', 'ESCC', 'GEA', 'HNSC', 'KIRCKICH', 'KIRP', 'LGGGBM', 'LIHCCHOL', 'LUAD', 'LUSC', 'MESO', 'OV', 'PAAD', 'PCPG', 'PRAD', 'SARC', 'SKCM', 'TGCT', 'THCA', 'THYM', 'UCEC', 'UVM'])


To view how many subtypes a cancer cohort has, example `BRCA`:
```
len(cancer2name['BRCA'].values())
```
> 4
