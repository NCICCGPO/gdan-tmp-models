# Common Issues and Errors
### Logging into Docker / Synapse Docker Registry
During set up, entering `docker login` or `docker login -u <synapse-username> docker.synapse.org` returns the error message:
```
Authenticating with existing credentials...
Login did not succeed, error: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
```

Check to make sure that Docker app is turned on.


### Logging into Synapse Docker Registry
During setup, entering `docker login -u <synapse-username> docker.synapse.org` returns the error message:
```
Error response from daemon: Get "https://docker.synapse.org/v2/": unauthorized: authentication required
```

Try logging out of Docker `docker logout`, logging back in `docker login`, and then reattempt Synapse Docker registry login `docker login -u <synapse-username> docker.synapse.org`


### Creating CWL Job File
During data preprocessing, running `bash RUN_model.sh <cancer> <platform> <method> <data>` returns the error message:
```
Invalid input combination, see options in tools/options.yml
```

The combination (`cancer`, `platform`, `method`) you requested is not available. Classifiers are built with a specific set of statistical or data type assumptions - therefore some combinations are not allowed. Look in `tools/options.yml` for the allowed combinations - organized by `method`, `cancer`, and then by `platform`.
