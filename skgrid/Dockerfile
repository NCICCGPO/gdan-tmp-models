FROM python:3.10
RUN pip install --upgrade pip
RUN pip install sklearn pandas pyyaml argparse numpy PyYAML

WORKDIR /skgrid/

COPY image_scripts  ./
COPY data ./data
COPY predict.sh prediction_runner.py pick_model.py select_model.yml ./
CMD chmod -R o+r ./
CMD chmod 777 ./image_scripts/train.sh
CMD chmod 755 ./select_model.yml

ENTRYPOINT ["/skgrid/image_scripts/train.sh"]

ENTRYPOINT ["/skgrid/predict.sh"]
