# Modified from https://github.com/coastalcph/treebank-leakage/blob/master/regress_from_spreadsheet.py

from sklearn.linear_model import LinearRegression as LinR
import sys
import numpy as np
from sklearn.model_selection import cross_val_score
import pickle


def main():
    with open(sys.argv[1], "rb") as f:
        leakage_dict = pickle.load(f)

    with open(sys.argv[2], "rt") as f:
        lines = [l.strip().split('\t') for l in f.readlines()[2:101]]

    y1 = 9 # UAS
    #y1 = 10 # LAS
    X = []
    Y = []
    for line in lines:
        treebank = line[0]
        if treebank in leakage_dict:
            X.append([leakage_dict[treebank]])
            Y.append(float(line[y1]))

    reg = LinR(normalize=False).fit(X, Y)
    print(reg.score(X, Y))
    print(cross_val_score(reg,X,Y,cv=3,scoring='explained_variance').mean())
    print(cross_val_score(reg,X,Y,cv=3,scoring='neg_mean_absolute_error').mean())

if __name__ == "__main__":
    main()