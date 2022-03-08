

rule all:
    input:
        "subscope.info",
        "aklimate.info",
        "cloudforest.info"

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
        "stuartlab_tmp_aklimate_20210714_docker_image.tar.gz"
    shell:
        "synapse get -r syn25982821 --downloadLocation aklimate/src/"

rule aklimate_docker_load:
    output:
        "aklimate.info"
    input:
        "stuartlab_tmp_aklimate_20210714_docker_image.tar.gz"
    shell:
        "docker load -i aklimate/src/stuartlab_tmp_aklimate_20210714_docker_image.tar.gz && docker tag 4befea59cb3b aklimate-tmp:latest && docker images | grep aklimate > aklimate.info"

rule cloudforest:
    output:
        "cloudforest.info"
    shell:
        "docker build -t cloudforest cloudforest/ && docker images | grep cloudforest > cloudforest.info"
