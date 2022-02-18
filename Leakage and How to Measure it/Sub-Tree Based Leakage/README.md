# Sub-Tree Based Leakage

## REUParsing.py
This contains many of the utility functions that we rely on for parsing and hashing CoNLL-U trees.

## POSmethods.py
These are utility functions used in Create_BFS_Dataset.py for subtree hashing.

## Create_BFS_Dataset.py
This creates the hashes from the treebanks, but at a subtree level. This uses functions from POSmethods.py to create the data.

## REULeakage.py
This contains many functions used for measuring leakage. These functions are used in ComputeLeakage.py.

## ComputeLeakage.py
This contains the functions to calculate a variety of types of leakage within and between languages. 
The vectors are prepared by running prepare_vectors which uses REULeakage.py. 
per_treebank_leakage calculates leakage from one languages test set into its own train set. 
cross_treebank_leakage calculates leakage from each treebank in the test set to all other training sets 
(used for multilingual models like UDify). inter_treebank_leakage is on an individual basis 
(each language has its leakage into each language calculated).

## Regress_From_Dictionaries.py
This is the main experiment which uses code from Søgaard to compute the explained variance and other measures on the leakage dictionaries created.

## Score Data:

### ud_spreadsheet.tsv
This is Søgaard's original spreadsheet with scores from each of the language models.

### UDify-Scores.tsv
This is the spreadsheet that has scores from UDify on various languages.

### UDPipe-Scores.tsv
This is the spreadsheet that has scores from UDPipe on various languages.
