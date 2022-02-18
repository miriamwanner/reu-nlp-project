# Reproducing Søgaard

## REUParsing.py
This contains many of the utility functions that we rely on for parsing and hashing CoNLL-U trees.

## GenerateHashFiles.py
This builds a dictionary with the hashes for each language in Universal Dependencies.

## REULeakage.py
This contains many functions used for measuring leakage. These functions are used in ComputeLeakage.py.

## ComputeLeakage.py
This contains the functions to calculate a variety of types of leakage within and between languages. The vectors are prepared by running prepare_vectors which uses REULeakage.py. per_treebank_leakage calculates leakage from one languages test set into its own train set. cross_treebank_leakage calculates leakage from each treebank in the test set to all other training sets (used for multilingual models like UDify). inter_treebank_leakage is on an individual basis (each language has its leakage into each language calculated).

## UDify_Leakage.py
It merges the hash dictionaries for languages used specifically in UDify. It computes the cross treebank leakage on these languages using ComputeLeakage.py.

## Regress_From_Dictionaries.py


## Score Data:

### ud_spreadsheet.tsv

### UDify-Scores.tsv

### UDPipe-Scores.tsv
