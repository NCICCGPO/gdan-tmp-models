#!/usr/bin/env python

import os
import sys
import pickle
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--data", help='data to make subtype predictions')
parser.add_argument("--output_prefix", help="output file prefix. will always end in _preds.tsv", default = '')
parser.add_argument("--model", nargs = '+',help="trained model pickle file")
args = parser.parse_args()

feat=pd.read_csv(args.data, sep="\t", index_col=0)

out = {}
for model in args.model:
    model_name = os.path.basename(model)
    obj = pickle.load(open(model, "rb"))
    X = feat[obj.feature_names_in_]

    labels = pd.Series(obj.predict(X), index=X.index, name="Labels")

    if hasattr(obj, "predict_proba"):
        for c, p in zip(obj.classes_, obj.predict_proba(X).T):
            out[model_name] = labels
            out["%s:%s" % (model_name, c)] = p
    else:
        out[model_name] = labels

df = pd.DataFrame(out)
df.to_csv(args.output_prefix + '_preds.tsv', sep="\t")
