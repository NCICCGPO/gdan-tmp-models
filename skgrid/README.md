# SK Grid
### Predicted Subtype Probabilities
Most models return the prediction probability for each subtype, where the overall predicted subtype is the one with the highest probability for the given sample. Due to the nature of the machine learning algorithm (ex. SVC, Passive aggressive, SGD, etc.) a few that do not return prediction probabilities will return only the overall predicted subtype.

### Feature Sets
The top SK Grid feature sets were selected based on highest weighted overall F1 performance regardless of feature set size (from the top of the top file and can be found on the publication page). Model ties were then broken by smallest standard deviation between cross folds. If ties still existed, then the model with the simplest hyperparameters/parameters was selected.
