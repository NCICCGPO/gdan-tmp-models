#!/usr/bin/env python

import os
import sys
import yaml
import json
import argparse

from sklearn.model_selection import ParameterGrid

from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.svm import SVC

classifers = {
    "sklearn.ensemble.AdaBoostClassifier": AdaBoostClassifier,
    "sklearn.naive_bayes.BernoulliNB": BernoulliNB,
    "sklearn.tree.DecisionTreeClassifier": DecisionTreeClassifier,
    "sklearn.ensemble.ExtraTreesClassifier": ExtraTreesClassifier,
    "sklearn.naive_bayes.GaussianNB": GaussianNB,
    "sklearn.gaussian_process.GaussianProcessClassifier": GaussianProcessClassifier,
    "sklearn.neighbors.KNeighborsClassifier": KNeighborsClassifier,
    "sklearn.linear_model.LogisticRegression": LogisticRegression,
    "sklearn.neural_network.MLPClassifier": MLPClassifier,
    "sklearn.naive_bayes.MultinomialNB": MultinomialNB,
    "sklearn.linear_model.PassiveAggressiveClassifier": PassiveAggressiveClassifier,
    "sklearn.ensemble.RandomForestClassifier": RandomForestClassifier,
    "sklearn.linear_model.SGDClassifier": SGDClassifier,
    "sklearn.svm.SVC": SVC
}

parser = argparse.ArgumentParser()
parser.add_argument("grid_config")
parser.add_argument("--outdir", default="config")
parser.add_argument("-n", default=1, type=int)

args = parser.parse_args()

with open(args.grid_config) as handle:
    config = yaml.load(handle, Loader=yaml.FullLoader)

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

for c in config:
    base = c['name'].split(".")[-1]
    n = args.n
    if 'n' in c:
        n = c['n']
    for i, chunk in enumerate(chunks(list(ParameterGrid(c['params'])), n)):
        with open(os.path.join(args.outdir, "%s.%d" % (base, i)), "w") as handle:
            for job in chunk:
                handle.write(json.dumps({"name" : c['name'], "params" : job}) + "\n")
