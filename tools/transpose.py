#!/usr/bin/python
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", help="input file, must be tsv")
args = parser.parse_args()

df = pd.read_csv(args.input, sep='\t', index_col=0).T
name = args.input.split('.')[:-1]
name.append('transposed.tsv')
name ='.'.join(name)
df.to_csv(name, sep='\t', index=True)
print(name) # stdout captured for RUN_MODEL.sh
