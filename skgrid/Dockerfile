FROM python:3.10

ARG BUILD_DATE
MAINTAINER Jordan Lee  <leejor@ohsu.edu>
LABEL version="1.0"
LABEL author="Jordan Lee <leejor@ohsu.edu>"
LABEL maintainer="Jordan Lee <leejor@ohsu.edu>"
LABEL org.label-schema.build-date=$BUILD_DATE
LABEL description="SK Grid Top Machine Learning Models for Predicting Cancer Subtype from Genomics/Molecular Data"

USER root
RUN pip install --upgrade pip && \
  pip install sklearn pandas pyyaml argparse numpy PyYAML

RUN groupadd -g 999 appuser && \
    useradd -r -u 999 -g appuser appuser
USER appuser
WORKDIR /skgrid/
COPY data ./data
COPY set_model_params.py create_grid.py \
  mlib.sh run_train.py train.sh predict.sh \
  prediction_runner.py pick_model.py \
  select_model.yml ./
