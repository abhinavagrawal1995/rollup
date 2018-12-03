from SlackAPIWrapper import getMessageData, getMessagesFromIndicies
from cluster import generateListOfMessages, getClusters
from textrank import textrank
import numpy as np
import re
import math
import json

def doMagic(userId, channelId, token):
    # Get all unseen messages
    data = getMessageData(channelId, token)

    messageTexts = []

    for message in data:
        txt = message['text'].decode('utf-8', 'ignore')
        messageTexts.append(txt)

    # # Group into clusters
    msgs = generateListOfMessages(data)
    clusterIndicies = getClusters(msgs)
    labels = clusterIndicies.keys()

    messageClusters = []
    for label in labels:
        indicies = clusterIndicies.get(label)
        cluster = []
        for index in indicies:
            cluster.append(messageTexts[index])
        messageClusters.append(cluster)

    # Find important clusters
    res = []
    for cluster in messageClusters:
        document = ""
        for message in cluster:
            document += message + " "

        text_ranks = textrank(document)

        numMessages = math.ceil(len(text_ranks) * .3)

        importantMessagesInCluster = []
        for i in range(int(numMessages)):
            item = {"text": text_ranks[i][1]}

            importantMessagesInCluster.append(item)
        res.append(importantMessagesInCluster)
    return res


def generateListOfMessages(data):
    listOfMessages = []
    for message in data:
        listOfMessages.append((message['ts'], 1))
    return listOfMessages