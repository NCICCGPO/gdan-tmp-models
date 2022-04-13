#!/usr/bin/python
# Requires access to GDAN TMP classifier_metrics_20210821 tarball
import pandas as pd

# Open large combined feature matrix
# Hardcoded bc this file has restricted access
ft_df = pd.read_csv('../../../../08_manuscript/featureSetML_TCGA/src/classifier_metrics_20210821/collected_features_matrix.tsv', sep='\t', low_memory=False)

# KIRCKICH,LGGGBM,LIHCCHOL does not have MIR only model
# MESO,OV,PAAD does not have MUTA model
cancer_list = [
    'ACC', 'BRCA', 'BLCA', 'CESC',
    'COADREAD', 'ESCC', 'GEA', 'HNSC',
    'KIRCKICH', 'KIRP', 'LGGGBM', 'LIHCCHOL',
    'LUAD', 'LUSC', 'MESO', 'OV',
    'PAAD', 'PCPG', 'PRAD', 'SARC',
    'SKCM', 'TGCT', 'THCA', 'THYM',
    'UCEC', 'UVM'
]

for cancer in cancer_list:

    # Find top model name and associated ftset name
    for platform in ['OVERALL','CNVR', 'GEXP', 'METH', 'MIR', 'MUTA']:

        # Not all cancers have all platforms - skip if no model
        if cancer in ['KIRCKICH', 'LGGGBM', 'LIHCCHOL'] and platform == 'MIR':
            print('...skipping {} for {} because no model ran'.format(cancer, platform))
            continue
        elif cancer in ['MESO', 'OV', 'PAAD'] and platform == 'MUTA':
            print('...skipping {} for {} because no model ran'.format(cancer, platform))
            continue
        else:
            df = pd.read_csv('./skgrid_best_models_{}_2022-04-05_v1.tsv'.format(platform), sep='\t')
            print(platform)
            top = df[df['Cohort']==cancer].reset_index()
            model = top['Model'][0]
            ftid = top['Features'][0]

            print(model)
            print(ftid)

            # Save ft names as a file
            output = '../data/src/training_data/{}_{}_featurelist.txt'.format(cancer, platform)
            with open(output, 'w') as out:
                s1 = ft_df[['featureID', ftid+'_'+cancer]]
                s1 = s1.iloc[3:,]
                s1 = s1.loc[(s1=='1').any(axis=1)]

                for a in s1['featureID']:
                    out.write(a +'\n')
