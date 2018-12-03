# cluster based on time threshold (kmeans)
# weightage, messageId

import json
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

from SlackAPIWrapper import getMessageData

def generateListOfMessages(data):
    listOfMessages = []
    for message in data:
        listOfMessages.append((message['ts'], 1))

    return listOfMessages

def getClusters(listOfMessages):
    X = np.asarray(listOfMessages)

    kmeans = KMeans()
    kmeans.fit(X)

    cluster_centers = kmeans.cluster_centers_
    labels = kmeans.labels_
    numLabels = len(cluster_centers)

    res = {}
    for label in range(numLabels):
        # kmeans returns a mapping of size X with labels 0-K representing which cluster they are in
        indicies = np.where(labels == label)
        res[label] = indicies[0].tolist()
    return res
