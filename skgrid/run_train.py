#!/usr/bin/env python
import numpy as np
np.random.seed(42)
import os
import sys
import gzip
import pandas as pd
import argparse
import pickle
import yaml
import json
from copy import copy
from sklearn.inspection import permutation_importance
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
from sklearn.gaussian_process.kernels import RBF
from sklearn.gaussian_process.kernels import DotProduct
from sklearn.gaussian_process.kernels import Matern
from sklearn.gaussian_process.kernels import RationalQuadratic
from sklearn.gaussian_process.kernels import WhiteKernel


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


gp_kernels = {
    "sklearn.gaussian_process.kernels.RBF" : RBF,
    "sklearn.gaussian_process.kernels.DotProduct": DotProduct,
    "sklearn.gaussian_process.kernels.Matern": Matern,
    "sklearn.gaussian_process.kernels.RationalQuadratic": RationalQuadratic,
    "sklearn.gaussian_process.kernels.WhiteKernel": WhiteKernel
}


def get_classifier(name, params):
    if name == "sklearn.gaussian_process.GaussianProcessClassifier":
        d = copy(params)
        d['kernel'] = gp_kernels[params['kernel']]()
        params = d
    return classifers[name](**params)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--ft_list', type=str, help="File with list of features to be used")
    parser.add_argument('--ft_file', type=str, help='Input path for feature file')
    parser.add_argument('--cancer', type=str, help='cancer cohort')
    parser.add_argument('--platform', type=str, help='platform of wanted model (ie GEXP, CNVR, MUTA, MIR, METH)')
    parser.add_argument('--model_file', type=str, help='json file of model parameter strings')
    args = parser.parse_args()

    configs = []
    with open(args.model_file) as handle:
        for line in handle:
            configs.append( json.loads(line) )

    # Train model
    for config in configs:
        name = config['name']
        params = config['params']
        clf = get_classifier(name, params)

        model_name = "%s-%s" % (
            config['name'].split(".")[-1],
            "_".join( "%s-%s" % (k,v) for k,v in config['params'].items() )
        )

        lst_file=pd.read_csv(args.ft_list, sep="\t", header=None)
        select_features = lst_file.iloc[:,0].to_list()
        print("Feature: ", select_features )
        print("loading feature matrix")
        feat=pd.read_csv(args.ft_file, sep="\t", index_col=0)
        print("subsetting matrix")
        X = feat[select_features]
        y = feat["Labels"]
        clf.fit(X, y)
        #clf.features_ = select_features
        pickle.dump( clf, open( os.path.join(model_name + ".model") , "wb" ) )
        # pickle.dump( clf, open( os.path.join(args.out, model_name + ".model") , "wb" ) )
