#!/usr/bin/bash

# specify input file
# cancer
# model platform

method=${1}

if [[ ${method} == 'jadbio' ]]
then
	tr '\t' ',' < example_inputs_cancers/example_BRCA.tsv > example_inputs_cancers/example_BRCA.csv
fi

cd ${method}
bash RUN.sh
