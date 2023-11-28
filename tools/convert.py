#!/usr/bin/python
# Purpose: create sample x TMP-feature-ID matrix
import pandas as pd
import numpy as np
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--cancer", help="cancer cohort")
parser.add_argument("--data", help="input data to be transformed, must be tsv")
parser.add_argument("--conversion_file", default='tools/ft_name_convert/entrez2tmp_BRCA_GEXP.json', help="conversion file to map input fts to TMP feature names. default value ideal for most cases")
parser.add_argument("--out", help="name of output file")
parser.add_argument("--delete_i_col", default=0, type=int, help="index number of col to remove, eg. 1. note this is zero based indexing. default is 0 for no deletion")
args = parser.parse_args()


# From cbioportal data - convert to TMP-ft-id and format
df = pd.read_csv(args.data, sep='\t')

# Filter out  extra info (optional)
df = df.iloc[:, args.delete_i_col:]

df = df.dropna()

# Open conversion file and convert
with open(args.conversion_file, 'r') as fh:
    entrez2tmp = json.load(fh)

tmp = []
for a in df['Entrez_Gene_Id']:
    try:
        tmp_ft = entrez2tmp[str(int(a))]
        tmp.append(tmp_ft)
    except:
        tmp.append(np.nan)

# Filter
df.insert(1, args.cancer, tmp)
df = df.iloc[:,1:]
df = df.dropna()
df.index=df[args.cancer]
df= df.iloc[:,1:]
df = df.transpose()

df.to_csv(args.out, sep='\t')
