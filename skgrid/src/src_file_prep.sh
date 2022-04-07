#!/usr/bin/bash
# Requires access to GDAN TMP classifier_metrics_20210821 tarball

# Create simple file of top model names
python names_model_ftsets.py

# Generate feature set files of top models
python generate_ft_lists.py
