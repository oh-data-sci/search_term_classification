import numpy as np
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC #(setting multi_class=”crammer_singer”)


def train_model(training_data_raw):
    """
    given training training data
    trains a `LinearSVC` model with discovered hyperparameters
    """
    tfidf = TfidfVectorizer(
        stop_words = {'english'},
        strip_accents= 'ascii',
        ngram_range=(1,1), # consider unigrams/bigrams/trigrams?
        min_df = 8,
        max_df = 0.9,
        binary = True, # count term occurance in each query only once
    )
    clf_svc = LinearSVC(
        dual=False,
        tol=1e-3,
        multi_class='ovr',
        max_iter=3000,
    )
    X = tfidf.fit_transform(training_data_raw['query'])
    y = training_data_raw['category']

    clf_svc.fit(X, y)
    
    return tfidf, clf_svc


def predictions_from_model(model, preprocessor, new_data_raw):
    """
    """
    try:
        y_predict = model.predict(preprocessor.transform(new_data_raw))
    except Exception as err:
        print('error computing model predictions using model', model)
        raise err
    return y_predict
