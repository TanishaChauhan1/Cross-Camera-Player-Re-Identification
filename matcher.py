import numpy as np
from scipy.spatial.distance import cosine

def extract_histogram(image):
    import cv2
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv], [0, 1], None, [50, 60], [0, 180, 0, 256])
    return cv2.normalize(hist, hist).flatten()

def compute_features(detections):
    features = {}
    for i, det in enumerate(detections):
        features[i] = extract_histogram(det['crop'])
    return features

def match_players(features1, features2):
    mapping = {}
    for id1, feat1 in features1.items():
        best_match = min(features2.items(), key=lambda item: cosine(feat1, item[1]))
        mapping[id1] = best_match[0]
    return mapping
