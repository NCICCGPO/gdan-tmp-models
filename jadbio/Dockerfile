FROM centos:8

ENV PATH=$PATH:/opt/java/jdk-15.0.2/bin

# Java requirement for JADBio
RUN mkdir /opt/java && \
    curl https://download.java.net/java/GA/jdk15.0.2/0d1cfde4252546c6931946de8db48ee2/7/GPL/openjdk-15.0.2_linux-x64_bin.tar.gz | tar -xz -C /opt/java/
