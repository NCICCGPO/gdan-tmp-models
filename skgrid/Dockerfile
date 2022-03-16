FROM python:3.10
RUN pip install --upgrade pip
RUN pip install sklearn pandas pyyaml argparse numpy

WORKDIR /skgrid/

COPY scripts  ./
COPY data ./data
COPY predict.sh run_learn.py prediction_runner.py ./
CMD chmod -R o+r ./
CMD chmod 777 ./scripts/train.sh

CMD ["./scripts/train.sh"]

ENTRYPOINT ["/skgrid/predict.sh"]
