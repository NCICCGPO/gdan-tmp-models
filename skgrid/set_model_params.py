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

parser = argparse.ArgumentParser()
parser.add_argument("--config", help='path to grid config yaml file')
parser.add_argument("--cancer", help='cancer abbrev (ex. BRCA)')
parser.add_argument("--platform", help='data platform abbrev (ex. GEXP)')
parser.add_argument("-n", default=1, type=int)
args = parser.parse_args()

n = args.n

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

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

# Load best model yaml
with open('select_model.yml', 'r') as handle:
    top_options = yaml.load(handle, Loader=yaml.FullLoader)
# Select best model
selected_model = top_options[args.cancer][args.platform]['file'].strip().split('/')[-1]
sel_name = selected_model.split('.')[1]
sel_n = int(selected_model.split('.')[2])

# Load full model library strings
with open(args.config) as handle:
    config = yaml.load(handle, Loader=yaml.FullLoader)

for c in config:
    base = c['name'].split(".")[-1]
#     if 'n' in c:
#         n = c['n']

    # Select model that matches selected model string
    if base ==sel_name:

        for i, chunk in enumerate(chunks(list(ParameterGrid(c['params']) ), n)):
            # Match i with model string n
            if sel_n==i:
                # print(base, n, c)
                # print()
                # print(i, chunk)
                # print()

                # Create and write model params
                with open(os.path.join("Classifier.%s.%d" % (base, i)), "w") as handle:
                    for job in chunk:
                        handle.write(json.dumps({"name" : c['name'], "params" : job}) + "\n")
