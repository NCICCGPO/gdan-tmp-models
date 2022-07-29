# JADBio
### Predictions file
Each run of a JADBio model produces a single csv results file, where the first column contains the sample ID, while the following columns contain the probability for each cancer subtype. The overall predicted subtype can be determined by taking the largest probability for each sample.

# Notes on platforms
JADBio does not include MIR models for `KIRCKICH`, `LGGGBM` or `LIHCCHOL`
