# Requirements

## 1. Required Applications

+ Install [Python 3+](https://www.python.org/downloads/)
+ Install [Docker Desktop](https://docs.docker.com/get-started/get-docker/) (or Docker)
+ Install [Synapse client](https://help.synapse.org/docs/Installing-Synapse-API-Clients.1985249668.html) and create an account
+ Install [AWS Client](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)


## 2. Create an environment and install dependencies. 
    
```bash
python3 -m venv venv; source venv/bin/activate
```

```bash
pip install --upgrade pip; pip install -r requirements.txt
```
> This will install `cwlref-runner` version 1.0, this specific version is required

## 3. Sign into Applications

Synapse Sign In

```bash
synapse login --remember-me
```

Docker Sign In (if not already)

```bash
docker login
```

Synapse Docker Registry Sign In - using Syanpse username and password

```bash
docker login -u <synapse-username> docker.synapse.org
```


## 4. Download Required Data

### 4.1 Tools Related Files

Navigate to [Publication Page under Supplemental Data](https://gdc.cancer.gov/about-data/publications/CCG-TMP-2022). Download the following files:

### 4.1.1. Place these files in `tools/`:

+ TMP_20230209.tar.gz
+ ft_name_convert.tar.gz
+ model_info.json

Then decompress files with: 

```bash
cd tools; tar -xzf TMP_20230209.tar.gz; cd ..

cd tools; tar -xzf ft_name_convert.tar.gz; cd ..
```

### 4.2 Model Files
Certain methods require large or source files to run models. These files are available for download.

Navigate to [Publication Page under Supplemental Data](https://gdc.cancer.gov/about-data/publications/CCG-TMP-2022). Download the files from the following sections

### 4.2.1 CloudForest Files 

Place this file in `cloudforest/data`:

+ models_cf.tar.gz

Then decompress files with: 
```bash
cd cloudforest/data; tar -xzf models_cf.tar.gz; cd ../..
```

### 4.2.2 JADBio Files 

Place this file in `jadbio/data`:

+ models_jadbio.tar.gz

Then decompress files with: 
```bash
cd cloudfojadbiorest/data; tar -xzf models_jadbio.tar.gz; cd ../..
```

### 4.2.2 SK Grid Files 

Create a copy of molecular data
```bash
cp -r tools/TMP_20230209 skgrid/data/src/training_data/
```

> Note: AKLIMATE and subSCOPE models do not need manual model data download


# Alternative Build Docker Images (Optional)
Docker images for methods are automatically pulled and built by CWL workflows and tools from the public Synapse repository.

Alternatively:
1. Docker images can be manually downloaded by going to the [Publication Page under Supplemental Data](https://gdc.cancer.gov/about-data/publications/CCG-TMP-2022) for each method image file.
```
# ImageFiles
sk_grid.tar.gz
aklimate.tar.gz
cloudforest.tar.gz
jadbio.tar.gz
subscope.tar.gz
```

2. Build each method's docker image.
```
docker load -i <imagefile.tar.gz>
```
Check these images have been successfully loaded with `docker images`.

Note that some methods have an additional model data file to run. These can be found at the [Publication Page under Supplemental Data](https://gdc.cancer.gov/about-data/publications/CCG-TMP-2022) (see section Download Method Model Data)

