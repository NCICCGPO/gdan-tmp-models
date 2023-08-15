#!/usr/bin/python
import pandas as pd
import argparse
import json

class ExtendAction(argparse.Action):

    def __call__(self, parser, namespace, values, option_string=None):
        items = getattr(namespace, self.dest) or []
        items.extend(values)
        setattr(namespace, self.dest, items)

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--platform',required = True, choices=['GEXP', 'MUTA', 'CNVR', 'METH', 'MIR'], help="platform (ex. GEXP)", type=str)
parser.add_argument('-i_dir', '--input_dir',required = False, help="input dir (ex. pred-alchemist)",  type=str)
parser.add_argument('-c','--cancer_list', action='append', help='<Required> Set flag, where each cancer is listed', required=True)
parser.add_argument('-m','--method_list', required=True, help='<Required> Set flag, where each method is listed', type=str)
parser.add_argument('-o_dir', '--output_dir',required = False, help="output dir (ex. pred-alchemist)",  type=str)
parser.add_argument('-i', '--infile',required = False, help="input file name",  type=str)
args = parser.parse_args()

print('Collating probabilities')
df = pd.read_csv(args.infile, sep='\t')

for cancer in args.cancer_list:
    for ml_method in args.method_list.split('.'):
        with open('tools/cancer2subtype.json', 'r') as fh:
            cancer2subtype = json.load(fh)
        probs = cancer2subtype[cancer]

        if ml_method == 'jadbio':
            file = '{}/{}/{}_{}_{}_preds.csv'.format(args.input_dir,cancer,cancer,args.platform, ml_method)
        elif ml_method == 'cloudforest':
            file = '{}/{}/{}_{}_{}_votes.vo'.format(args.input_dir,cancer,cancer,args.platform, ml_method)
        else:
            file = '{}/{}/{}_{}_{}_preds.tsv'.format(args.input_dir,cancer,cancer,args.platform, ml_method)

        outfile = '{}/midway/{}_{}_format2.tsv'.format(args.output_dir,ml_method, cancer)

        s1 = df[df['method']==ml_method]
        s1 = s1[s1['TCGA_cohort']==cancer].reset_index(drop=True)

        # Remove extra data and rename
        s1[ml_method+'_call']= s1['subtype_prediction']
        s1 = s1.drop(['method', 'subtype_prediction'], axis =1)

        if ml_method == 'skgrid':
            # begin reading in file info
            preds = pd.read_csv(file, sep='\t', index_col=0)
            samples = list(preds.index)
            for sample in samples:
                # For one sample at a time, grab the subtype probs for this ONE method
                s2=preds.loc[sample,]
                for i in range(1,s2.shape[0]):
                    subtype = s2.index[i].strip().split(':')[1]
                    p = s2[i]
                    probs[subtype].append(p)
            # Append col for corresponding cancer
            # if that subtype never called by method, then skip adding that results col
            for k,v in probs.items():
                try:
                    s1['skgrid:'+k]= v
                except:
                    continue
            s1.to_csv(outfile, sep='\t', index=False)
        if ml_method == 'jadbio':
            # begin reading in file info
            preds = pd.read_csv(file, sep=',', index_col=0)
            samples = list(preds.index)
            for sample in samples:
            #     For one sample at a time, grab the subtype probs for this ONE method
                s2=preds.loc[sample,]
                for i in range(0,s2.shape[0]):
                    subtype = s2.index[i].split('=')[1].strip().split(' ')[0].replace(':','_')
                    p = s2[i]
                    probs[subtype].append(p)
            # Append col for corresponding cancer
            # if that subtype never called by method, then skip adding that results col
            for k,v in probs.items():
                try:
                    s1['jadbio:'+k]= v
                except:
                    continue
            s1.to_csv(outfile, sep='\t', index=False)
        if ml_method == 'aklimate':
            # begin reading in file info
            preds = pd.read_csv(file, sep='\t', index_col=0)
            samples = list(preds.index)
            for sample in samples:
            #     For one sample at a time, grab the subtype probs for this ONE method
                s2=preds.loc[sample,]
                for i in range(1,s2.shape[0]):
                    subtype = s2.index[i]
                    p = s2[i]
                    probs[subtype].append(p)
            # Append col for corresponding cancer
            # if that subtype never called by method, then skip adding that results col
            for k,v in probs.items():
                try:
                    s1['aklimate:'+k]= v
                except:
                    continue
            s1.to_csv(outfile, sep='\t', index=False)
        if ml_method == 'subscope':
            # begin reading in file info
            preds = pd.read_csv(file, sep='\t', index_col=0)
            samples = list(preds.index)
            for sample in samples:
            #     For one sample at a time, grab the subtype probs for this ONE method
                s2=preds.loc[sample,]
                for i in range(0,s2.shape[0]):
                    subtype = s2.index[i].strip().split('|')[0]
                    p = s2[i]
                    probs[subtype].append(p)

            # Append col for corresponding cancer
            # if that subtype never called by method, then skip adding that results col
            for k,v in probs.items():
                try:
                    s1['subscope:'+k]= v
                except:
                    continue
            s1.to_csv(outfile, sep='\t', index=False)
        if ml_method == 'cloudforest':
            preds = pd.read_csv(file, sep='\t', index_col=0)
            total = list(preds.transpose().sum())
            preds['N']= total
            samples = list(preds.index)
            for sample in samples:
            #     For one sample at a time, grab the subtype probs for this ONE method
                s2=preds.loc[sample,]
                for i in range(0,s2.shape[0]-1):
                    subtype = s2.index[i].strip().split('|')[0]
                    p = (s2[i])/s2['N']
                    probs[subtype].append(p)
            # Append col for corresponding cancer
            # if that subtype never called by method, then skip adding that results col
            for k,v in probs.items():
                try:
                    s1['cloudforest:'+k]= v
                except:
                    continue
            s1.to_csv(outfile, sep='\t', index=False)
