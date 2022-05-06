#!/usr/bin/bash

# Example: bash RUN_model.sh BRCA GEXP cloudforest user-transformed-data/transformed-data.tsv
cancer=${1}
platform=${2}
method=${3}
data=${4}

# Create cwl job yaml - WIP only for cloudforest for now
python tools/create_jobs.py --cancer ${cancer} --platform ${platform} --method ${method} --data ${data}  --outname ${cancer}'_'${platform}'_'${method}'_preds.tsv'


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
