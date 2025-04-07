# Additional Info: Model Selection and Input Specifications
Each the file in `user-job-ymls/` is associated with the method and is automatically generated from `RUN_MODEL.sh`.

> Available methods are `skgrid`, `aklimate`, `cloudforest`, `jadbio`, and `subscope`.

Each method file is slightly different, but all will require selection of at least the input dataset, cancer model, and data platform. Available values are noted in [tools/options.yml](../tools/options.yml).

Model platform name differs for each method, see below:

## SK Grid options
+ Model options: `OVERALL`, `CNVR`, `GEXP`, `METH`, `MIR`, or `MUTA`
+ `GEXP` best model that uses only mRNA expression (gene expression) for predictions
+ `CNVR` best model that uses only copy number variation for predictions
+ `METH` best model that uses only DNA methylation for predictions
+ `MIR` best model that uses only miRNA for predictions
+ `MUTA` best model that uses only somatic mutations for predictions
+ `OVERALL` best model regardless of platform (can be single data platform type or a combination of platforms).
+ Additional method details found in [SK Grid README](../skgrid/README.md)

## AKLIMATE options
+ Model options: `TOP`, `GEXP`, `CNVR`, `METH`, or `MULTI`
+ `GEXP` best model that uses only mRNA expression (gene expression) for predictions
+ `CNVR` best model that uses only copy number variation for predictions
+ `METH` best model that uses only DNA methylation for predictions
+ `MIR` best model that uses only miRNA for predictions
+ `MUTA` best model that uses only somatic mutations for predictions
+ `TOP` best model regardless of platform (can be single data platform type or a combination of platforms). *(recommended over MULTI)*
+ `MULTI` best model *can* use all available data types (CNVR, GEXP, METH, MIR, and MUTA)
+ Additional method details found in [AKLIMATE README](../aklimate/README.md)

## CloudForest options
+ Model options: `OVERALL`, `All`, `CNVR`, `GEXP`, `METH`, `MIR`, or `MUTA`
+ `GEXP` best model that uses only mRNA expression (gene expression) for predictions
+ `CNVR` best model that uses only copy number variation for predictions
+ `METH` best model that uses only DNA methylation for predictions
+ `MIR` best model that uses only miRNA for predictions
+ `MUTA` best model that uses only somatic mutations for predictions
+ `OVERALL` best model regardless of platform (this can be a model that uses a single platform, several platforms, or all platforms; it simply returns the model that had the highest performance). *(recommended over MULTI)*
+ `All` best model *must* use all available data types (CNVR, GEXP, METH, MIR, and MUTA)
+ Additional method details found in [CloudForest README](../cloudforest/README.md)

## subSCOPE options
+ Model options: `allcohorts`, `CNVR`, `GEXP`, `METH`, `MIR`, or `MUTA`
+ `GEXP` best model that uses only mRNA expression (gene expression) for predictions
+ `CNVR` best model that uses only copy number variation for predictions
+ `METH` best model that uses only DNA methylation for predictions
+ `MIR` best model that uses only miRNA for predictions
+ `MUTA` best model that uses only somatic mutations for predictions
+ `allcohorts` best model that can predict on a mixed cancer cohort (ex. pancreatic tumors can be mixed with breast tumors). Will return the best subtype predictions regardless of cohort
+ Additional method details found in [subSCOPE README](../subscope/README.md)

## JADBio options
+ Model options: `MULTI`, `CNVR`, `GEXP`, `METH`, `MIR`, or `MUTA`
+ `GEXP` best model that uses only mRNA expression (gene expression) for predictions
+ `CNVR` best model that uses only copy number variation for predictions
+ `METH` best model that uses only DNA methylation for predictions
+ `MIR` best model that uses only miRNA for predictions
+ `MUTA` best model that uses only somatic mutations for predictions
+ `MULTI` best model that *must* use all available data types
+ Additional method details found in [JADBio README](../jadbio/README.md)
