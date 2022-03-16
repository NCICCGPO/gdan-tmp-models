FROM python:3.10
RUN pip install --upgrade pip
RUN pip install sklearn pandas pyyaml argparse numpy

WORKDIR /skgrid/

COPY image_scripts  ./
COPY data ./data
COPY predict.sh prediction_runner.py ./
CMD chmod -R o+r ./
CMD chmod 777 ./image_scripts/train.sh

ENTRYPOINT ["/skgrid/image_scripts/train.sh"]

ENTRYPOINT ["/skgrid/predict.sh"]
