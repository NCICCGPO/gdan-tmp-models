#!/usr/bin/python
# Purpose: create sample x TMP-feature-ID matrix
import pandas as pd
import numpy as np
import json

### Hardcoded
cancer = 'BRCA'
out = 'user-transformed-data/TEST_cbioportal_BRCA_GEXP.tsv'
###

# From cbioportal data - convert to TMP-ft-id and format
file = 'brca_metabric/data_mrna_agilent_microarray.txt'
df = pd.read_csv(file, sep='\t')

# Filter out  extra info and nan
df = df.iloc[:, 1:]
df = df.dropna()

# Open conversion file and convert
with open('tools/entrez2tmp_BRCA_GEXP.json', 'r') as fh:
    entrez2tmp = json.load(fh)

tmp = []
for a in df['Entrez_Gene_Id']:
    try:
        tmp_ft = entrez2tmp[str(int(a))]
        tmp.append(tmp_ft)
    except:
        tmp.append(np.nan)

# Filter
df.insert(1, cancer, tmp)
df = df.iloc[:,1:]
df = df.dropna()
df.index=df[cancer]
df= df.iloc[:,1:]
df = df.transpose()

df.to_csv(out, sep='\t')
