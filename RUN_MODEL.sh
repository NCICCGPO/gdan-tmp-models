#!/usr/bin/bash

method=${1}

if [[ ${method} == 'jadbio' ]]
then
	tr '\t' ',' < example_inputs_cancers/example_BRCA.tsv > example_inputs_cancers/example_BRCA.csv
fi


if [[ ${method} == 'cloudforest' ]]
# TODO update this for all methods
then
	cd ${method}
	bash RUN.sh user-transformed-data/transformed-data.tsv
else
	cd ${method}
	bash RUN.sh
fi
