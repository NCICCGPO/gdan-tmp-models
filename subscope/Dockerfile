FROM subscope
RUN chmod 777 /src/predict.sh
RUN chmod -R o+r /src

COPY data /data
RUN chmod -R 777 /data
RUN chmod -R o+rw /data
