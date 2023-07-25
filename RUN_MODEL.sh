#!/usr/bin/bash

# Example: bash RUN_model.sh BRCA GEXP cloudforest user-transformed-data/transformed-data.tsv
# Example: bash RUN_MODEL.sh BRCA GEXP aklimate example_inputs_cancers/example_BRCA.tsv
# Example: bash RUN_MODEL.sh BRCA GEXP skgrid user-transformed-data/transformed-data.tsv
# Example: bash RUN_MODEL.sh BRCA GEXP subscope example_inputs_cancers/example_BRCA.tsv
# Example: bash RUN_MODEL.sh BRCA GEXP jadbio example_inputs_cancers/example_BRCA.tsv

set -e
cancer=${1}
platform=${2}
method=${3}
data=${4}

# Prep file - transpose (should already be scaled/transformed)
echo 'Checking if transposed required'
if [[ ${method} == 'cloudforest' ]]
then
	data_transposed=$(python tools/transpose.py --input ${data})
fi

# Format prep
echo 'Checking if field separation required'
if [[ ${method} == 'jadbio' ]]
then
	tdata_name=$(echo ${data} | sed "s/.tsv/.csv/g")
	tr '\t' ',' < ${data} > ${tdata_name}
fi

# Create cwl job yaml
echo 'Creating cwl job yaml'
if [[ ${method} == 'aklimate' || ${method} == 'subscope' ]]
then
	python tools/create_jobs.py --cancer ${cancer} --platform ${platform} --method ${method} --data ${data}
elif [[ ${method} == 'cloudforest' ]]
then
	python tools/create_jobs.py --cancer ${cancer} --platform ${platform} --method ${method} --data ${data_transposed}  --outname ${cancer}'_'${platform}'_'${method}
elif [[ ${method} == 'jadbio' ]]
then
	python tools/create_jobs.py --cancer ${cancer} --platform ${platform} --method ${method} --data ${tdata_name}  --outname ${cancer}'_'${platform}'_'${method}
else
	python tools/create_jobs.py --cancer ${cancer} --platform ${platform} --method ${method} --data ${data}  --outname ${cancer}'_'${platform}'_'${method}
fi



# Run cwl workflow
echo 'Starting machine learning job'
cd ${method}
bash RUN.sh
