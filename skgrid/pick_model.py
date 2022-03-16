#!/usr/bin/python

import yaml
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--cancer", help="cancer cohort of the skgrid model to use")
parser.add_argument("--platform",help="data platform (i.e. GEXP, MUTA, MIR, CNVR, METH) of the skgrid model to use ")
args = parser.parse_args()

with open('/skgrid/select_model.yml', 'r') as fh:
    try:
        modelconfig = yaml.safe_load(fh)
    except yaml.YAMLError as exc:
        print(exc)

model = modelconfig[args.cancer][args.platform]
print(model)
