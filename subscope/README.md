# SubSCOPE   
### Job Input Platform Options   

Allowed platform types (Required input):   
+ MIR, MUTA, GEXP, CNVR, or METH
+ Note: MIR is not available for KIRCKICH and LIHCCHOL

Allowed TCGA Cancer cohort (Optional input):   
+ ACC, BLCA, BRCA, CESC, COADREAD, ESCC, GEA, HNSC, KIRCKICH, KIRP, LGGGBM, LIHCCHOL, LUAD, LUSC, MESO, OV, PAAD, PCPG, PRAD, SARC, SKCM, TGCT, THCA, THYM, UCEC, UVM   
> If no cohort is passed, pan-cancer predictions are made.   

User Data Format:   
+ First row gives feature IDs.  
+ First column gives sample IDs.  

### Job Outputs  
Two files are generated at `subscope/data/preds/`. The best subtype predictions are included in `subscope/data/preds/<platform>-subscope-results.txt`.    
Note that both outputs will be pre-filtered for only the Cohort of interest, if you specified a TCGA Cancer cohort.  
+ `<platform>-subscope-results.txt` : First column is sample IDs, Second column is the best prediction.    

+ `<platform>-subscope-confidence.txt` : First column is sample IDs, subsequent columns are confidence values for each of the prediction classes.     