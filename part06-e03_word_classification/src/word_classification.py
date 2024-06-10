#!/usr/bin/env python3
from collections import Counter
import urllib.request
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection

alphabet="abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)

def load_finnish():
    finnish_url="https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename="src/kotus-sanalista_v1.xml"
    load_from_net=False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines=[]
            for line in data:
                lines.append(line.decode('utf-8'))
        doc="".join(lines)
    else:
        with open(filename, "rb") as data:
            doc=data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))

def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines=map(lambda s: s.rstrip(), data.readlines())
    return lines

def get_features(a):
    feature_matrix = np.zeros((len(a), 29))
    for i, word in enumerate(a):
        for char in word:
            if char in alphabet:
                feature_matrix[i, alphabet.index(char)] += 1
    
    return feature_matrix

def contains_valid_chars(s):
    for char in s:
        if char not in alphabet:
            return False
    
    return True

def get_features_and_labels():
    eng_words = load_english()
    fin_words = load_finnish()

    fin_words = [word.lower() for word in fin_words]
    fin_words = [word for word in fin_words if contains_valid_chars(word)]

    eng_words = [word for word in eng_words if word[0].islower()]
    eng_words = [word.lower() for word in eng_words]
    eng_words = [word for word in eng_words if contains_valid_chars(word)]

    all_words = np.array(fin_words + eng_words)
    X = get_features(all_words)
    
    y = np.array(len(fin_words) * [0] + len(eng_words) * [1])

    return X, y

def word_classification():
    X, y = get_features_and_labels()
    model = MultinomialNB()
    k_cv = model_selection.KFold(n_splits=5, shuffle=True, random_state=0)
    cv_score = cross_val_score(model, X, y, cv=k_cv)
    return cv_score

def main():
    print("Accuracy scores are:", word_classification())

if __name__ == "__main__":
    main()