#!/usr/bin/python

# Create cwl job yaml
import argparse
import glob

parser = argparse.ArgumentParser()
parser.add_argument("--method", help="method (ex. cloudforest, jadbio, skgrid, subscope, aklimate)")
parser.add_argument("--data",help="transformed user data to get predictions for")
parser.add_argument("--cancer", help="cancer cohort of the skgrid model to use")
parser.add_argument("--platform", help="data platform (i.e. GEXP, MUTA, MIR, CNVR, METH, etc)")
parser.add_argument("--outname",required = False, help="name of output prediction file")
args = parser.parse_args()


if args.method == 'cloudforest':
    # Pull CF file name specific to inputs
    files = glob.glob('cloudforest/data/{}/{}/*.sf'.format(args.cancer, args.platform))
    if len(files)==1:
        rf_file = files[0]
    elif len(files)==0:
        print('The specified cancer or platform is not avaible for CloudForest')
    else:
        print('ERROR multiple files found')
    # Write job file
    with open('user-job-ymls/cloudforest-inputs.yml', 'w') as fh:
        fh.write('fm_input:\n')
        fh.write('  - class: File\n')
        fh.write('    path: ../{}\n'.format(args.data))
        fh.write('rfpred_input:\n')
        fh.write('  - class: File\n')
        fh.write('    path: ../{}\n'.format(rf_file))
        fh.write('preds_input:\n')
        fh.write('  - {}\n'.format(args.outname))
