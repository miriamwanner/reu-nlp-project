# Leakage Explains 0-Shot Performance
This folder contains the code used for the corresponding section in the paper.

## Data Creation
This contains the code used to prepare the data for the experiments. The hashes are created, in order to identify isomorphisms. 
These hashes are then divided based on whether they leak. The hashes are used to split the data into leaky and non-leaky bins.
The data is then trimmed so the bins are the same size. 
For an additional experiment, there is another dataset created for diverse tree data (the data contains only one of each type of tree structure).

## Experiments
This folder contains the README explaining how to run the experiments, because the code was all external.
