#!/usr/bin/python

# Create cwl job yaml
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--method", help="method (ex. cloudforest, jadbio, skgrid, subscope, aklimate)")
parser.add_argument("--data",help="transformed user data to get predictions for")

parser.add_argument("--rfpred",required = False, help="Cloud Forest specific")
parser.add_argument("--outname",required = False, help="name of output prediction file")

parser.add_argument("--platform",required= False, help="data platform (i.e. GEXP, MUTA, MIR, CNVR, METH, etc)")
parser.add_argument("--cancer", required= False, help="cancer cohort of the skgrid model to use")
args = parser.parse_args()


if args.method == 'cloudforest':
    with open('user-job-ymls/cloudforest-inputs.yml', 'w') as fh:
        fh.write('fm_input:\n')
        fh.write('  - class: File\n')
        fh.write('    path: ../{}\n'.format(args.data))
        fh.write('rfpred_input:\n')
        fh.write('  - class: File\n')
        fh.write('    path: ../{}\n'.format(args.rfpred))
        fh.write('preds_input:\n')
        fh.write('  - {}\n'.format(args.outname))
