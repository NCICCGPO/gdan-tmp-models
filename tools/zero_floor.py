#!/usr/bin/python

import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-in', '--input',required = True, help="input file name",  type=str)
parser.add_argument('-out', '--output',required = True, help="output file name",  type=str)
parser.add_argument('-s', '--sep',default = '\t', required = False, help="separation field of input, default is tab separated",  type=str)
parser.add_argument('-index', '--indexcol',default = 0, required = False, help="index_col value for reading in pandas df, default is 0",  type=int)
args = parser.parse_args()

def check_neg(df):
    '''check if negative values exist in at least once in matrix'''
    low =0
    for i in range(0, df.shape[1]):
        data = min(df[df.columns[i]])
        #immediately exit if find a negative number
        if data<low:
            #low= data
            return('negative')
    return('no_negative')


df_values = pd.read_csv(args.input, sep=args.sep, index_col=args.indexcol)
if check_neg(df_values) == 'negative':
    print('found negative values, applying 0 flooring')
    # Floor all negative values to 0
    df_values[df_values < 0] = 0
    # Sanity check again
    assert check_neg(df_values) == 'no_negative'
# save
df_values.to_csv(args.output, sep='\t', index=True)
