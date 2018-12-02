from SlackAPIWrapper import getMessageData, getMessagesFromIndicies, getUser, getUsernameFromUserId
from cluster import generateListOfMessages, getClusters
from textrank import textrank
import numpy as np
import re
import math
import json
def main(userId, channel, token):
    # Get all unseen messages
    token = "xoxp-487248075381-493930035239-494364886471-9b84b3bb946d4788f3d443c713f6c27a"
    data = getMessageData("CEB1EAGN6", token)

    messageTexts = []

    for message in data:
        txt = message['text'].decode('utf-8', 'ignore')

        # start = txt.find('<')
        # end = txt.find('>')
        # if start != -1 and end != -1:
        #     txt = txt[start + 1:end]
        #
        # txt = re.sub('[^A-Za-z0-9 \.]+', '', txt)
        # txt = txt.encode('utf-8', 'ignore')
        messageTexts.append(txt)

    # print(messageTexts)
    # # Group into clusters
    clusterIndicies = getClusters(generateListOfMessages(data))
    # print(clusterIndicies)

    labels = clusterIndicies.keys()

    res = []
    for label in labels:
        indicies = clusterIndicies.get(label)
        na = np.array(messageTexts)
        nb = np.array(indicies)
        out = list(na[nb])

        document = ""
        for message in out:
            document += message + " "

        textrankresult = textrank(document)


        threshhold = math.ceil(len(textrankresult) * .3)
        clusterResults = []
        result = {}
        for i in range(int(threshhold)):
            result["text"] = textrankresult[i][1]
            clusterResults.append(result)

        res.append(clusterResults)

    return res


def generateListOfMessages(data):
    listOfMessages = []
    for message in data:
        listOfMessages.append((message['ts'], 1))
    return listOfMessages


results = main(None, None, None)

