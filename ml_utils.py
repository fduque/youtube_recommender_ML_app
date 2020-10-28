import pandas as pd
import re
import joblib as jb
from scipy.sparse import hstack, csr_matrix
import numpy as np
import json

mapa_meses = {"jan": "Jan",
              "fev": "Feb",
              "mar": "Mar",
              "abr": "Apr",
              "mai": "May",
              "jun": "Jun",
              "jul": "Jul",
              "ago": "Aug",
              "set": "Sep",
              "out": "Oct",
              "nov": "Nov",
              "dez": "Dec"}

#models to be applied
mdl_rf = jb.load("models/random_forest_20201028.pkl.z")
mdl_lgbm = jb.load("models/lgbm_20201028.pkl.z")
title_vec = jb.load("models/title_vectorizer_20201028.pkl.z")

#TODO: Refactor clea_date function.
def clean_date(data):
    """Data transform for datatime convertion"""
    if re.search(r"(\d+) de ([a-z]+)\. de (\d+)", data['watch-time-text']) is None:
        return None
        # if date is null return none

    raw_date_str_list = list(re.search(r"(\d+) de ([a-z]+)\. de (\d+)", data['watch-time-text']).groups())
    # print(raw_date_str_list)
    if len(raw_date_str_list[0]) == 1:
        raw_date_str_list[0] = "0" + raw_date_str_list[0]

    raw_date_str_list[1] = mapa_meses[raw_date_str_list[1]]

    clean_date_str = " ".join(raw_date_str_list)

    return pd.to_datetime(clean_date_str, format="%d %b %Y")

#TODO: Refactor clean_view function.
def clean_views(data):
    """Will return qty of views for each video"""
    raw_views_str = re.match(r"(\d+\.?\d*)", data['watch-view-count'])
    if raw_views_str is None:
        return 0
    raw_views_str = raw_views_str.group(1).replace(".", "")
    # print(raw_views_str)

    return int(raw_views_str)


def compute_features(data):
    """Will process the features to be used by the model"""
    if 'watch-view-count' not in data:
        return None

    publish_date = clean_date(data)
    if publish_date is None:
        return None

    views = clean_views(data)
    title = data['watch-title']

    features = dict()
    #calc qty of days since published
    features['tempo_desde_pub'] = (pd.Timestamp.today() - publish_date) / np.timedelta64(1, 'D')
    features['views'] = views
    features['views_por_dia'] = features['views'] / features['tempo_desde_pub']
    del features['tempo_desde_pub']

    #transforming title in a vector
    vectorized_title = title_vec.transform([title])

    #csr_matrix is good choice to be used for general projects
    num_features = csr_matrix(np.array([features['views'], features['views_por_dia']]))
    feature_array = hstack([num_features, vectorized_title])

    return feature_array


def compute_prediction(data):
    """Will return the prediction score for each video"""
    feature_array = compute_features(data)

    #TODO: Refactor to be more reliable
    if feature_array is None:
        return 0

    p_rf = mdl_rf.predict_proba(feature_array)[0][1]
    p_lgbm = mdl_lgbm.predict_proba(feature_array)[0][1]

    #compound model to be applied
    p = 0.5 * p_rf + 0.5 * p_lgbm
    # log_data(data, feature_array, p)

    return p


def log_data(data, feature_array, p):
    """"Function to be used in production to monitor the model."""
    # print(data)
    video_id = data.get('og:video:url', '')
    data['prediction'] = p
    data['feature_array'] = feature_array.todense().tolist()
    # print(video_id, json.dumps(data))







