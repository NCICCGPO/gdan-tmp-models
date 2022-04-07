#!/usr/bin/python
# Requires access to GDAN TMP classifier_metrics_20210821 tarball


# Extract best SK_Grid model for both:
    # All data types
    # Best single platform

import pandas as pd

# Hardcoded bc this file has restricted access
metrics = pd.read_csv( '../../../../08_manuscript/featureSetML_TCGA/src/classifier_metrics_20210821/big_results_matrix.tsv', sep='\t', low_memory=False)
metrics = metrics[metrics.model.str.contains('skgrid')]
metrics = metrics[metrics.performance_metric.str.contains('overall_weighted_f1')]

# 1. Best Overall model
store_dict_26_by_3 = {'Cohort':[], 'Model':[], 'Features':[]}
for c in metrics.cohort.unique():
    cFrame = metrics[metrics.cohort == c].copy()
    cFrame.reset_index(inplace=True,drop = True)
    cFrame.sort_values(['Mean', 'Std'], ascending=[False, True],
                      inplace = True)
    cFrame.reset_index(inplace=True,drop = True)
    best_cohort_model = cFrame.loc[0,'model']
    features = cFrame.loc[0,'featureID']
    store_dict_26_by_3['Cohort'].append(c)
    store_dict_26_by_3['Model'].append(best_cohort_model)
    store_dict_26_by_3['Features'].append(features)
bestSK = pd.DataFrame(data = store_dict_26_by_3, index = list(range(0,26)))
# Fix the model names (optional)
formatted_models = bestSK.copy()
for i, model in enumerate(bestSK.Model):
    clf = model.split('|')[0].split('_', 1)[1]
    formatted_models.iloc[i, 1] = clf
# Remove trailing cohort tag from feature set name
formatted_models_feature_sets = formatted_models.copy()
for i, raw_feat_name in enumerate(formatted_models_feature_sets.Features):
    feature_set = raw_feat_name.rsplit('_', 1)[0]
    formatted_models_feature_sets.iloc[i, 2] = feature_set
formatted_models_feature_sets.to_csv(
    'skgrid_best_models_OVERALL_2022-04-05_v1.tsv',
    sep = '\t', index = False)

# 2. Best model for each data platform
# Just one platform; from over-written metrics objects
for input_plat in ['CNVR', 'GEXP', 'METH', 'MIR', 'MUTA']:
    print('working on {}'.format(input_plat))
    metrics_plat = metrics[metrics.model.str.contains(input_plat)].copy()

    store_dict_26_by_3 = {'Cohort':[], 'Model':[], 'Features':[]}
    for c in metrics_plat.cohort.unique():
        cFrame = metrics_plat[metrics_plat.cohort == c].copy()
        cFrame.reset_index(inplace=True,drop = True)

        cFrame.sort_values(['Mean', 'Std'], ascending=[False, True],
                          inplace = True)

        cFrame.reset_index(inplace=True,drop = True)
        best_cohort_model = cFrame.loc[0,'model']
        features = cFrame.loc[0,'featureID']
        store_dict_26_by_3['Cohort'].append(c)
        store_dict_26_by_3['Model'].append(best_cohort_model)
        store_dict_26_by_3['Features'].append(features)

    # Some cancer cohorts weren't ran for all 5 single platform types
    n_cancers = len(store_dict_26_by_3['Cohort'])
    if n_cancers != 26:
        print('{} only had {} out of 26 cancer cohorts'.format(input_plat, n_cancers))
    bestSKplat = pd.DataFrame(data = store_dict_26_by_3, index = list(range(0,n_cancers)))




    # Fix the model names; remonve leading cohort (optional)
    formatted_models_plat = bestSKplat.copy()
    for i, model in enumerate(bestSKplat.Model):
        clf = model.split('|')[0].split('_', 1)[1]
        formatted_models_plat.iloc[i, 1] = clf



    # Remove trailing cohort tag from feature set name (optional)
    formatted_models_feature_sets_plat = formatted_models_plat.copy()
    for i, raw_feat_name in enumerate(formatted_models_feature_sets_plat.Features):
        feature_set = raw_feat_name.rsplit('_', 1)[0]
        formatted_models_feature_sets_plat.iloc[i, 2] = feature_set


    # Save
    formatted_models_feature_sets_plat.to_csv(
        'skgrid_best_models_{}_2022-04-05_v1.tsv'.format(input_plat),
        sep = '\t', index = False)
