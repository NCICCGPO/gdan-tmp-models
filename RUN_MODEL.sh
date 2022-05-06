#!/usr/bin/bash

# bash RUN_model.sh cloudforest user-transformed-data/transformed-data.tsv
method=${1}
data=${2}


# Create cwl job yaml - WIP only for cloudforest for now
python tools/create_jobs.py --method ${method} --data ${data} --rfpred 'cloudforest/data/BRCA/GEXP/GEXP_50_R4_F1.sf' --outname 'BRCA_GEXP_cloudforest_preds.tsv'


if [[ ${method} == 'jadbio' ]]
then
	tr '\t' ',' < example_inputs_cancers/example_BRCA.tsv > example_inputs_cancers/example_BRCA.csv
fi


if [[ ${method} == 'cloudforest' ]]
# TODO update this for all methods
then
	cd ${method}
	bash RUN.sh ${data}
else
	cd ${method}
	bash RUN.sh
fi
