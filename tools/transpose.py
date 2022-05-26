#!/usr/bin/python
import os.path
from os import path
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", help="input file, must be tsv")
args = parser.parse_args()

# Potential output name
name = args.input.split('.')[:-1]
name.append('transposed.tsv')
name ='.'.join(name)


# Check if transposed file does not exist
if path.exists(name) == False:
    # Transpose
    df = pd.read_csv(args.input, sep='\t', index_col=0).T
    df.to_csv(name, sep='\t', index=True)

print(name) # stdout captured for RUN_MODEL.sh
