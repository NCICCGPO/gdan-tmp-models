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
    # Test if user inputs valid
    assert args.platform in method_options[args.method][args.cancer], 'Invalid input combination, see options in tools/options.yml'
    # Generate cwl job input file
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
    # Test if user inputs valid
    assert args.platform in method_options[args.method][args.cancer], 'Invalid input combination, see options in tools/options.yml'
    # Generate cwl job input file
    with open('user-job-ymls/aklimate-inputs.yml', 'w') as fh:
        fh.write('cancer:\n')
        fh.write('  - {}\n'.format(args.cancer))
        fh.write('platform:\n')
        fh.write('  - {}\n'.format(args.platform))
        fh.write('input_data:\n')
        fh.write('  - class: File\n')
        fh.write('    path: ../{}\n'.format(args.data))

elif args.method == 'cloudforest':
    # Test if user inputs valid
    print(method_options[args.method][args.cancer], args.platform)
    assert args.platform in method_options[args.method][args.cancer], 'Invalid input combination, see options in tools/options.yml'
    # Pull CF file name specific to inputs
    files = glob.glob('cloudforest/data/models_cf/{}/{}/*.sf'.format(args.cancer, args.platform))
    if len(files)==1:
        rf_file = files[0]
    elif len(files)==0:
        print('The specified cancer or platform is not avaible for CloudForest')
    else:
        print('ERROR multiple files found')
    # Generate cwl job input file
    with open('user-job-ymls/cloudforest-inputs.yml', 'w') as fh:
        fh.write('fm_input:\n')
        fh.write('  - class: File\n')
        fh.write('    path: ../{}\n'.format(args.data))
        fh.write('rfpred_input:\n')
        fh.write('  - class: File\n')
        fh.write('    path: ../{}\n'.format(rf_file))
        fh.write('preds_input:\n')
        fh.write('  - {}_preds.tsv\n'.format(args.outname))
        fh.write('votes_input:\n')
        fh.write('  - {}_votes.vo\n'.format(args.outname))

elif args.method == 'subscope':
    # Test if user inputs valid
    assert args.platform in method_options[args.method][args.cancer], 'Invalid input combination, see options in tools/options.yml'
    # Generate cwl job input file
    with open('user-job-ymls/subscope-inputs.yml', 'w') as fh:
        fh.write('cancer:\n')
        fh.write('  - {}\n'.format(args.cancer))
        fh.write('platform:\n')
        fh.write('  - {}\n'.format(args.platform))
        fh.write('input_data:\n')
        fh.write('  - class: File\n')
        fh.write('    path: ../{}\n'.format(args.data))

elif args.method == 'jadbio':
    # Test if user inputs valid
    assert args.platform in method_options[args.method][args.cancer], 'Invalid input combination, see options in tools/options.yml'
    # Generate cwl job input file
    with open('user-job-ymls/jadbio-inputs.yml', 'w') as fh:
        fh.write('model:\n')
        fh.write('  - class: File\n')
        fh.write('    path: ../jadbio/data/models_jadbio/{}_{}_model.bin\n'.format(args.cancer, args.platform))
        fh.write('input_data:\n')
        fh.write('  - class: File\n')
        fh.write('    path: ../{}\n'.format(args.data))
        fh.write('out:\n')
        fh.write('  - {}_preds.csv\n'.format(args.outname))
