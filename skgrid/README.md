# Note to developing SK Grid Docker Image

If creating SK Grid feature lists from scratch
```
cd src
python src_file_prep.sh
```

However, this requires access to GDAN TMP `classifier_metrics_20210821` tarball. The output files of `src_file_prep.sh` 
are already included in the Docker image under `data/src/training_data/` so users will not need to run these scripts
