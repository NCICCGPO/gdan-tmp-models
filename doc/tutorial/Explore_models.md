# Explore the Machine Learning Models

### Retrieve Machine Learning Model Information
Use the `get_model_info(method, platform, cancer)` from the tools_ml module.
```
import sys
sys.path.append('tools/')
import tools_ml


# Example: top model of SK Grid, gene expression only model for breast cancer
tools_ml.get_model_info('skgrid', 'GEXP', 'BRCA')
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

Options `platform` are ['GEXP', 'CNVR', 'MIR', 'MUTA', 'METH', 'OVERALL', 'All']. Note 'OVERALL' and 'All' are for CloudForest only

Options `cancer` are ['ACC', 'BLCA', 'BRCA', 'CESC', 'COADREAD', 'ESCC', 'GEA', 'HNSC', 'KIRCKICH', 'KIRP', 'LGGGBM', 'LIHCCHOL', 'LUAD', 'LUSC', 'MESO', 'OV', 'PAAD', 'PCPG', 'PRAD', 'SARC', 'SKCM', 'TGCT', 'THCA', 'THYM', 'UCEC', 'UVM']
