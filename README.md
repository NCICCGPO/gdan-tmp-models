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


# Cloud Forest ML
### Build Docker Image
Create docker image for Cloud Forest models (multi-stage build)
```
cd cloud-forest/
```
```
docker image build --tag cloudforest .
```

### Run Model
Cloud forest machine learning model can be ran as a CWL workflow
```
bash RUN.sh
```
