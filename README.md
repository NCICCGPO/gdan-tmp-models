# Setup

Create environment and setup
```
python -m venv venv
. venv/bin/activate

conda install python==3.8
```

Synapse and AWS
```
synapse login --remember-me
```

create `~/.aws/credentials`

```
[default]
aws_access_key_id=XXX
aws_secret_access_key=XXX
```


# Build Docker Image
Create docker image for Cloud Forest models (multi-stage build)
```
cd cloud-forest/
```
```
docker image build --tag cloudforest .
```


# Run ML Models
### TEMP - Cloud Forest Interactive Container
Start an interactive docker container and run Cloud Forest models
```
# Start interactive container
docker run -ti --rm -v `pwd`:/transfer -u `id -u` cloudforest
```
```
# Set up
chmod 755 transfer/CF_For_Docker/KIRCKICH/run_all.sh
cd /transfer

# Run models
CF_For_Docker/KIRCKICH/run_all.sh

exit
```
Results data in `cloud-forest/CF_For_Docker/KIRCKICH/CL` (25 files)


### WIP - Cloud Forest Automated with CWL
trying out first updating the dockerfile so last line is RUN instead of CMD
```
# build stage
FROM golang:1.17.2-alpine AS build-env
RUN apk add make git bash build-base
ENV GOPATH=/go
ENV PATH="/go/bin:${PATH}"
RUN go install github.com/ryanbressler/CloudForest/applyforest@latest

# final stage
FROM alpine
ENV PATH="/app:${PATH}"
COPY --from=build-env /go/bin/applyforest /app/

# analysis
ADD CF_For_Docker/ /CF_For_Docker/
RUN chmod 755 /CF_For_Docker/KIRCKICH/run_all.sh
RUN cd /
RUN CF_For_Docker/KIRCKICH/run_all.sh
```

then `docker image build --tag cloudforest .`

`docker run cloudforest` this runs without error but no output files locally. might need to mount a volume to persist the data



now
```
pip install cwlref-runner
```


```
docker run -ti --rm -v `pwd`:/transfer -u `id -u` cloudforest

cd transfer/cloud-forest/

cwl-runner docker.cwl docker-job.yaml
```
