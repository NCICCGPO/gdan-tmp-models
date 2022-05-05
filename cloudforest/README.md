# CloudForest

### How the Top Model was Selected
While filtering the best model from the csv files provided, when the mean
success was the same, the one with smaller standard deviation was selected.  If both mean and
standard deviation were the same, the one with lower feature size was selected. If still there
was a tie, gene expression was selected.

After running the models, the predictions in repeat-fold pairs were checked
and the one with the highest F1 score was picked. And it was double checked that success
was higher than the one reported in the mean success reported in model
accuracy  csv files for the best models per cohort - datatype pair and per
cohort.


### Files
.cl is the output file extension, .sf is the model file extension  and .fm
is input data extension.


### Model Notations
`MULTI` stands for using all available data types, `ALL` stands for using
all data for one datatype like gene expression.

An `OVERALL` folder was added in each cohort folder, which has the best model
for the cohort. When the `OVERALL` best was `MULTI` type, there will be a `MULTI`
folder in that tissue folder.
