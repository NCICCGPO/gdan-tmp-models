#!/usr/bin/env python

import os
import sys
import pickle
import pandas as pd

input = sys.argv[1]
output = sys.argv[2]
models = sys.argv[3:]

feat=pd.read_csv(input, sep="\t", index_col=0)

out = {}
for model in models:
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
if output == "-":
    df.to_csv(sys.stdout, sep="\t")
else:
    df.to_csv(output, sep="\t")
