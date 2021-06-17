import REUParsing as rp
import REULeakage as rl
import numpy as np
import pickle
import conllu
import networkx as nx
from tqdm import tqdm
from matplotlib import pyplot as plt
from scipy.spatial import distance
import os
import sys

MIN_TREES = 1

def main():
    if len(sys.argv) < 5:
        print("Usage: [train hashes] [test hashes] [cross-treebank out] [per-treebank out]")
        exit()
    # Load the hash dictionaries
    with open(sys.argv[1], "rb") as lf:
        language_hashes_train = pickle.load(lf)
    with open(sys.argv[2], "rb") as lf:
        language_hashes_test = pickle.load(lf)

    # Compute a combined dictionary
    language_hashes = {}
    for language in language_hashes_train:
        if language not in language_hashes:
            language_hashes[language] = {}
        for hash_ in language_hashes_train[language]:
            if hash_ not in language_hashes[language]:
                language_hashes[language][hash_] = language_hashes_train[language][hash_]
            else:
                language_hashes[language][hash_] += language_hashes_train[language][hash_]
    for language in language_hashes_test:
        if language not in language_hashes:
            language_hashes[language] = {}
        for hash_ in language_hashes_test[language]:
            if hash_ not in language_hashes[language]:
                language_hashes[language][hash_] = language_hashes_test[language][hash_]
            else:
                language_hashes[language][hash_] += language_hashes_test[language][hash_]

    # Compute the counts and remove any treebanks with fewer than MIN_TREES
    train_counts = rl.language_counts(language_hashes_train)
    for lang in train_counts:
        if train_counts[lang] < MIN_TREES:
            del language_hashes_train[lang]
    train_counts = {}
    for lang in language_hashes_train:
        train_counts[lang] = 0
        for hash_ in language_hashes_train[lang]:
            train_counts[lang] += language_hashes_train[lang][hash_]
            
    test_counts = rl.language_counts(language_hashes_test)
    for lang in test_counts:
        if test_counts[lang] < MIN_TREES:
            del language_hashes_test[lang]
    test_counts = {}
    for lang in language_hashes_test:
        test_counts[lang] = 0
        for hash_ in language_hashes_test[lang]:
            test_counts[lang] += language_hashes_test[lang][hash_]
            
    all_counts = rl.language_counts(language_hashes)
    for lang in all_counts:
        if all_counts[lang] < MIN_TREES:
            del language_hashes[lang]
    all_counts = {}
    for lang in language_hashes:
        all_counts[lang] = 0
        for hash_ in language_hashes[lang]:
            all_counts[lang] += language_hashes[lang][hash_]

    # Compute the relative hash counts
    relative_train = rl.relative_hashes(language_hashes_train, train_counts)
    relative_test = rl.relative_hashes(language_hashes_test, test_counts)
    relative_all = rl.relative_hashes(language_hashes, all_counts)

    # Create a vocab of hashes we have seen
    hash_vocab = rl.generate_hash_vocab(relative_all)

    # Generate vectors
    print("Generating 'train' vectors...")
    train_vectors = rl.language_vectors(relative_train, hash_vocab)
    print("Generating 'test' vectors...")
    test_vectors = rl.language_vectors(relative_test, hash_vocab)

    print("Computing cross-treebank leakages...")
    language_leakages = {}
    for language in tqdm(test_vectors):
        group = {lang:train_vectors[lang] for lang in train_vectors if lang != language}
        language_leakages[language] = rl.leakage(test_vectors[language], group)

    with open(sys.argv[3], "wb") as f:
        pickle.dump(language_leakages, f)

    print("Computing per-treebank leakages...")
    per_language_leakages = {}
    for language in tqdm(test_vectors):
        if language in train_vectors:
            per_language_leakages[language] = rl.leakage(test_vectors[language], {language:train_vectors[language]})
        else:
            per_language_leakages[language] = -1

    with open(sys.argv[4], "wb") as f:
        pickle.dump(per_language_leakages, f)

if __name__ == "__main__":
    main()