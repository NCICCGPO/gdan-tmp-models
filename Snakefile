

rule all:
    input:
        "subscope.info",
        "aklimate.info",
        "cloudforest.info",
        "jadbio.info",
        "skgrid.info"

rule subscope_docker:
    output:
        "dockerimage-subscope-ccg-tmp.tar.gz"
    shell:
        "synapse get syn26284209"

rule subscope_docker_load:
    output:
        "subscope.info"
    input:
        "dockerimage-subscope-ccg-tmp.tar.gz"
    shell:
        "docker load -i dockerimage-subscope-ccg-tmp.tar.gz && docker images | grep subscope > subscope.info"

rule aklimate_docker:
    output:
        "aklimate/src/stuartlab_tmp_aklimate_20220407_docker_image.tar.gz"
    shell:
        "synapse get -r syn29280221 --downloadLocation aklimate/src/"

rule aklimate_docker_load:
    output:
        "aklimate.info"
    input:
        "aklimate/src/stuartlab_tmp_aklimate_20220407_docker_image.tar.gz"
    shell:
        "docker load -i aklimate/src/stuartlab_tmp_aklimate_20220407_docker_image.tar.gz && docker tag 881bb86c6cfd aklimate-tmp:latest && docker images | grep aklimate > aklimate.info"

rule cloudforest:
    output:
        "cloudforest.info"
    shell:
        "docker build -t cloudforest cloudforest/ && docker images | grep cloudforest > cloudforest.info"

rule jadbio_java:
    output:
        "jadbio/src/jadbio-model-exe.jar"
    shell:
        "synapse get -r syn27367851 --downloadLocation jadbio/src/"

rule jadbio_docker_load:
    output:
        "jabio.info"
    input:
        "jadbio/src/jadbio-model-exe.jar"
    shell:
        "docker build -t jadbio . && docker images | grep jadbio > jadbio.info"

rule skgrid_docker:
    output:
        "skgrid/src/skgrid_ohsu_docker_image.tar.gz"
    shell:
        "synapse get -r syn29294147 --downloadLocation skgrid/src/"

rule skgrid_docker_load:
    output:
        "skgrid.info"
    input:
        "skgrid/src/skgrid_ohsu_docker_image.tar.gz"
    shell:
        "docker load -i skgrid/src/skgrid_ohsu_docker_image.tar.gz && docker tag 0904b98ca996 skgrid:latest && docker images | grep skgrid > skgrid.info"
