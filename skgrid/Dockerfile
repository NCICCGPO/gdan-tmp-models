FROM python:3.10
RUN pip install --upgrade pip
RUN pip install sklearn pandas pyyaml argparse numpy

WORKDIR /skgrid/

COPY create_grid.py run_learn.py runner.py run_train.py train.sh  ./
COPY data/src ./data/src
COPY data/output/model_library ./data/output/model_library
COPY data/output/train ./data/output/train
CMD chmod -R o+r ./
CMD chmod 777 ./train.sh

CMD ["./train.sh"]
