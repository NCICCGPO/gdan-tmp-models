#!/bin/bash

# # outputs to current dir in results
# docker run --rm -v $(pwd):/data subscope BRCA GEXP /data/data/input/metabric_tmprescale.tsv

# # not work anymore
# docker run -i -v $(pwd):/transfer --read-only=false --rm subscope BRCA GEXP /transfer/data/input/metabric_tmprescale.tsv

# works
# docker run -i --env=HOME=/ --read-only=false --rm subscope BRCA GEXP data/input/metabric_tmprescale.tsv



# run cwl tool
cwl-runner --outdir data/preds \
  workflows/ml_workflow.cwl \
  job_inputs/subscope-inputs.yml

# # works
# docker run --rm -v $(pwd):/data --env=HOME=/data subscope BRCA GEXP /data/data/input/metabric_tmprescale.tsv
#

# rmeoved
# requirements:
#   InitialWorkDirRequirement:
#     listing:
#       - $(inputs.input_data)
