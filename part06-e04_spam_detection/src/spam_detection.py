#!/usr/bin/env python3
import  gzip
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import numpy as np

def spam_detection(random_state=0, fraction=0.1):
    ham = []
    with gzip.open('src/ham.txt.gz') as ns_f:
        ham_lines = ns_f.readlines()
        rec_lines = int(len(ham_lines) * fraction)
        ham = [line for i, line in enumerate(ham_lines) if i < rec_lines]
    
    spam = []
    with gzip.open('src/spam.txt.gz') as s_f:
        spam_lines = s_f.readlines()
        rec_lines = int(len(spam_lines) * fraction)
        spam = [line for i, line in enumerate(spam_lines) if i < rec_lines]

    data = ham + spam

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(data).toarray()
    y = len(ham) * [0] + len(spam) * [1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75, random_state=random_state)

    model = MultinomialNB()
    model.fit(X_train, y_train)
    y_predict = model.predict(X_test)
    acc = accuracy_score(y_test, y_predict)
    misclassified  = np.sum(y_test != y_predict)
    
    return acc, len(X_test), misclassified 

def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")

if __name__ == "__main__":
    main()