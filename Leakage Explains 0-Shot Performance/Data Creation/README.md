# Creating data for "Leakage Explains 0-Shot Performance"

## REUParsing.py:
This contains many of the utility functions that we rely on for parsing and hashing CoNLL-U trees.
<Add explanations of these functions>

## \<Hashing stuff from hard drive\>: UPDATE THIS
Make the hash dictionaries...

## SplitHashes.py:
This splits the leaky and non-leaky hashes from the train, dev, and test hash dictionaries.
These will be used to split the treebanks later into leaky and non-leaky groups.

## SplitTreebanks.py:
This uses the split hash dictionaries from SplitHashes.py to split the treebanks into leaky and non-leaky groups such that the leaky train and test treebanks have 100% train-test leakage.

## TrimData.py:
This trims the leaky and non-leaky training sets so that they are the same size to prevent data size from having a role in parser performance.

## DiversifyData.py:
This creates a "diverse" treebank for each language which contains only 1 of each tree structure.
