#!/usr/bin/python
# TODO update with commandline transpose
import pandas as pd
df = pd.read_csv('user-transformed-data/transformed-data.tsv', sep='\t', index_col=0).T
df.to_csv('user-transformed-data/transformed-data-transposed.tsv', sep='\t',
index=True)
