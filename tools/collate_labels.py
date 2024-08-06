#!/usr/bin/python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--platform',required = True, choices=['GEXP', 'MUTA', 'CNVR', 'METH', 'MIR', 'OVERALL', 'MULTI'], help="platform (ex. GEXP)", type=str)
parser.add_argument('-c','--cancer_list', action='append', help='<Required> Set flag, where each cancer is listed', required=True)
parser.add_argument('-i_dir', '--input_dir',required = False, help="input dir (ex. pred-alchemist)",  type=str)
parser.add_argument('-o', '--outfile',required = False, help="output file name",  type=str)
parser.add_argument('-m','--method_list', required=True, help='<Required> Set flag, where each method is listed', type=str)
args = parser.parse_args()

print('Collating labels')

# Initiate results file
with open(args.outfile, 'w') as out:
    out.write('sampleID\tsubtype_prediction\tTCGA_cohort\tplatform\tmethod\n')

for TCGA_cohort in args.cancer_list:
    for ml_method in args.method_list.split('.'):
        if ml_method == 'jadbio':
            file = '{}/{}/{}_{}_jadbio_preds.csv'.format(args.input_dir,TCGA_cohort,TCGA_cohort,args.platform)
        else:
            file = '{}/{}/{}_{}_{}_preds.tsv'.format(args.input_dir,TCGA_cohort,TCGA_cohort,args.platform, ml_method)
        # Append to results file
        with open(args.outfile, 'a') as out:
            with open(file, 'r') as fh:
                if ml_method == 'skgrid':
                    # No header info needed
                    fh.readline()
                    # Extract info from remaining lines
                    for line in fh:
                        line = line.strip().split('\t')
                        sampleID = line[0]
                        subtype_prediction = line[1]
                        # Append results
                        out.write('{}\t{}\t{}\t{}\t{}\n'.format(sampleID,subtype_prediction, TCGA_cohort, args.platform, ml_method))
                if ml_method == 'cloudforest':
                    # No header in this format
                    # Extract info from each line
                    for line in fh:
                        line = line.strip().split('\t')
                        sampleID= line[0]
                        subtype_prediction=line[1]
                        # Temp fix
                        model_details=ml_method
                        # Append results
                        out.write('{}\t{}\t{}\t{}\t{}\n'.format(sampleID,subtype_prediction, TCGA_cohort, args.platform, ml_method))
                if ml_method== 'jadbio':
                    # Extract header info
                    header = fh.readline().split(',')
                    for line in fh:
                        line = line.strip().split(',')
                        sampleID=line[0]
                        probabilty_tracker ={'prob':0, 'subtype':'init'}
                        for i in range(1,len(header)):
                            if float(line[i])>probabilty_tracker['prob']:
                                probabilty_tracker['prob']=float(line[i])
                                label = header[i].strip().split('=')[-1].split(' ')[1]
                                if ':' in label:
                                    assert label.split(':')[0]==TCGA_cohort
                                    label = '_'.join(label.split(':'))
                                elif '_' in label:
                                    assert label.split('_')[0]==TCGA_cohort
                                probabilty_tracker['subtype']=label
                        subtype_prediction = probabilty_tracker['subtype']
                        # Append results
                        out.write('{}\t{}\t{}\t{}\t{}\n'.format(sampleID,subtype_prediction, TCGA_cohort, args.platform, ml_method))
                if ml_method=='aklimate':
                    # No header info needed
                    fh.readline()
                    for line in fh:
                        line = line.strip().split('\t')
                        sampleID=line[0]
                        subtype_prediction=line[1]
                        # Append results
                        out.write('{}\t{}\t{}\t{}\t{}\n'.format(sampleID,subtype_prediction, TCGA_cohort, args.platform, ml_method))
                if ml_method=='subscope':
                    # No header info needed
                    fh.readline()
                    for line in fh:
                        line = line.strip().split('\t')
                        sampleID=line[0]
                        subtype_prediction=line[1].split('|')[0]
                        # Append results
                        out.write('{}\t{}\t{}\t{}\t{}\n'.format(sampleID,subtype_prediction, TCGA_cohort, args.platform, ml_method))
