# Explore the Machine Learning Models

### Retrieve Machine Learning Model Information
First download the required file to look into the model info, this file can be downloaded from the Publication Page: `model_info.json` (synapseID syn51321047)


Use the `get_model_info(method, platform, cancer)` from the tmp_convert module.
```
import sys
sys.path.append('tools/')
import tmp_convert


# Example: top model of SK Grid, gene expression only model for breast cancer
tmp_convert.get_model_info('skgrid', 'GEXP', 'BRCA')
```

Will return:
```
{'model': 'sklearn.ensemble.RandomForestClassifier',
 'model_params': {'criterion': 'entropy', 'n_estimators': 200},
 'fts': ['N:GEXP::CENPA:1058:',
  'N:GEXP::FOXC1:2296:',
  'N:GEXP::ESR1:2099:',
  'N:GEXP::MBOAT1:154141:',
  'N:GEXP::MIA:8190:',
  'N:GEXP::ANXA3:306:',
  'N:GEXP::WDR67:93594:',
  'N:GEXP::NAT1:9:',
  'N:GEXP::EXO1:9156:']}
```

### Allowed Options
`get_model_info(method, platform, cancer)` allows for:

Options `method` are ['skgrid', 'aklimate', 'cloudforest', 'subscope', 'jadbio']

Options `platform` are ['GEXP', 'CNVR', 'MIR', 'MUTA', 'METH']

Options `cancer` are ['BRCA', 'LGGGBM', 'COADREAD', 'SKCM', 'ACC', 'BLCA', 'CESC', 'ESCC', 'GEA', 'HNSC', 'KIRCKICH', 'KIRP', 'LIHCCHOL', 'LUAD', 'LUSC', 'MESO', 'OV', 'PAAD', 'PCPG', 'PRAD', 'SARC', 'TGCT', 'THCA', 'THYM', 'UCEC', 'UVM']
