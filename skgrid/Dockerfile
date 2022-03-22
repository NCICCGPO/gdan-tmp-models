FROM python:3.10
RUN pip install --upgrade pip
RUN pip install sklearn pandas pyyaml argparse numpy PyYAML

WORKDIR /skgrid/

COPY image_scripts  ./
COPY data ./data
COPY run_train.py train.sh predict.sh prediction_runner.py pick_model.py select_model.yml ./
RUN chmod -R o+rw ./
RUN chmod 777 ./train.sh
RUN chmod 777 ./run_train.py
RUN chmod 755 ./select_model.yml

#ENTRYPOINT ["/skgrid/image_scripts/train.sh"]

#ENTRYPOINT ["/skgrid/predict.sh"]
