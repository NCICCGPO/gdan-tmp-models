#!/usr/bin/python

# Create cwl job yaml
import argparse
import glob
import yaml

parser = argparse.ArgumentParser()
parser.add_argument("--method", help="method (ex. cloudforest, jadbio, skgrid, subscope, aklimate)")
parser.add_argument("--data",help="transformed user data to get predictions for")
parser.add_argument("--cancer", help="cancer cohort of the skgrid model to use")
parser.add_argument("--platform", help="data platform (i.e. GEXP, MUTA, MIR, CNVR, METH, etc)")
parser.add_argument("--outname",required = False, help="name of output prediction file")
args = parser.parse_args()

# Allowed input combos
with open('tools/options.yml', 'r') as fh:
    method_options = yaml.safe_load(fh)

if args.method == 'skgrid':
    if args.platform not in ['OVERALL', 'CNVR', 'GEXP', 'METH', 'MIR', 'MUTA']:
        print('Error: recieved platform {} --- platform must be OVERALL, CNVR, GEXP, METH, MIR, or MUTA for SK Grid'.format(args.platform))
        exit
    else:
        with open('user-job-ymls/skgrid-inputs.yml', 'w') as fh:
            fh.write('cancer:\n')
            fh.write('  - {}\n'.format(args.cancer))
            fh.write('platform:\n')
            fh.write('  - {}\n'.format(args.platform))
            fh.write('input_data:\n')
            fh.write('  - class: File\n')
            fh.write('    path: ../{}\n'.format(args.data))
            fh.write('output_prefix:\n')
            fh.write('  - {}\n'.format(args.outname))

elif args.method == 'aklimate':
    if args.platform not in ['TOP', 'GEXP', 'CNVR', 'METH', 'MULTI']:
        print('Error: recieved platform {} --- platform must be TOP, GEXP, CNVR, METH, or MULTI for AKLIMATE'.format(args.platform))
        exit
    else:
        with open('user-job-ymls/aklimate-inputs.yml', 'w') as fh:
            fh.write('cancer:\n')
            fh.write('  - {}\n'.format(args.cancer))
            fh.write('platform:\n')
            fh.write('  - {}\n'.format(args.platform))
            fh.write('input_data:\n')
            fh.write('  - class: File\n')
            fh.write('    path: ../{}\n'.format(args.data))

elif args.method == 'cloudforest':
    if args.platform not in method_options['cloudforest'][args.cancer]:
        print('Error: recieved platform {} --- platform must be OVERALL, MULTI, CNVR, GEXP, METH, MIR, or MUTA for CloudForest'.format(args.platform))
        exit
    else:
        # Pull CF file name specific to inputs
        files = glob.glob('cloudforest/data/{}/{}/*.sf'.format(args.cancer, args.platform))
        if len(files)==1:
            rf_file = files[0]
        elif len(files)==0:
            print('The specified cancer or platform is not avaible for CloudForest')
        else:
            print('ERROR multiple files found')
        with open('user-job-ymls/cloudforest-inputs.yml', 'w') as fh:
            fh.write('fm_input:\n')
            fh.write('  - class: File\n')
            fh.write('    path: ../{}\n'.format(args.data))
            fh.write('rfpred_input:\n')
            fh.write('  - class: File\n')
            fh.write('    path: ../{}\n'.format(rf_file))
            fh.write('preds_input:\n')
            fh.write('  - {}_preds.tsv\n'.format(args.outname))

elif args.method == 'subscope':
    if args.platform not in ['CNV', 'GEXP', 'METH', 'MIR', 'MUTA']:
        print('Error: recieved platform {} --- platform must be CNV, GEXP, METH, MIR, or MUTA for SubSCOPE'.format(args.platform))
        exit
    else:
        with open('user-job-ymls/subscope-inputs.yml', 'w') as fh:
            fh.write('cancer:\n')
            fh.write('  - {}\n'.format(args.cancer))
            fh.write('platform:\n')
            fh.write('  - {}\n'.format(args.platform))
            fh.write('input_data:\n')
            fh.write('  - class: File\n')
            fh.write('    path: ../{}\n'.format(args.data))
