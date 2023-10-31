#!/usr/bin/python
import argparse
import pandas as pd
from statistics import multimode
import statistics

print('Formating')
parser = argparse.ArgumentParser()
parser.add_argument('-i_dir', '--input_dir',required = False, help="input dir (ex. pred-alchemist)",  type=str)
parser.add_argument('-c','--cancer', required=True, help='<Required> Set flag, where each cancer is listed', type=str)
parser.add_argument('-m','--method_list', required=True, help='<Required> Set flag, where each method is listed', type=str)
parser.add_argument('-o', '--outfile',required = True, help="output file name",  type=str)
args = parser.parse_args()

# combine all 5 methods together
results_d = {}
for m in args.method_list.split('.'):
    results_d[m] = pd.read_csv('{}/midway/{}_{}_format2.tsv'.format(args.input_dir, m, args.cancer), sep='\t', index_col=0)
methods = list(results_d.keys())
first = 1
for method,df in results_d.items():
    if first == 1:
        base = df
        first = 0
    else:
        base = pd.merge(base, df, on=['sampleID', 'TCGA_cohort', 'platform'], how='outer')

# all absolute sample subtype call column
# this shows the most voted-for subtype
cols = list(map(lambda x: x + '_call', methods ))
s1 = base[cols]
final_subtype_call=[]
no_ties_col=[]
for s in s1.index:
    values = base.loc[s]
    final_call = multimode(s1.loc[s,])
    # if vote resulted in tie
    if len(final_call)>1:
        final_call.sort()
        # ties not allowed
        best = ['nan',0]
        for subtype in final_call:
            confidence_list = []
            for method in methods:
                conf = values[method + ':'+ subtype]
                confidence_list.append(float(conf))
            subtype_mean = statistics.mean(confidence_list)
            # if larger model confidence mean, update
            if subtype_mean > best[1]:
                best = [subtype, subtype_mean]
        # save single subtype and tied details
        no_ties_col.append(best[0])
        final_call = ':'.join(final_call)
        final_subtype_call.append(final_call)
    # if vote didnt result in tie
    else:
        final_call = ':'.join(final_call)
        no_ties_col.append(final_call)
        final_subtype_call.append(final_call)
base.insert(2, 'group_prediction_details', final_subtype_call)
base.insert(0, 'subtype', no_ties_col)

# Save
base.to_csv(args.outfile, sep='\t', index=True)
print('created final file:', args.outfile)
