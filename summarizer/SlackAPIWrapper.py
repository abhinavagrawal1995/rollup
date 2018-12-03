import requests
import json
from difflib import SequenceMatcher


def getRequestData(url):
    try:
        data = requests.get(url).text
    except requests.exceptions.RequestException as e:
        return None
    return data


def getConversationDataByChannel(base_url, channelId):
    url = base_url + "&channel=" + channelId + "&pretty=1"
    return getRequestData(url)


def getMessageData(channelId, token):
    channel_list_request = "https://slack.com/api/channels.list?token=" + token + "&pretty=1"
    message_list_per_channel_request = "https://slack.com/api/conversations.history?token=" + token + "&count=100"
    channelsJson = getRequestData(channel_list_request)
    jsonParser = json.loads(channelsJson)



    data = []
    conversationJson = getConversationDataByChannel(message_list_per_channel_request, channelId)
    jsonParser = json.loads(conversationJson)
    messages = jsonParser["messages"]
    for message in messages:
        if "subtype" not in message:
            data.append({
                # 'client_msg_id': message["client_msg_id"].encode('utf-8'),
                'ts': message["ts"].encode('utf-8'),
                'text': message["text"].encode('utf-8').replace("\n", ""),
                'user': message["user"].encode('utf-8')
            })

    return data

def getMessagesFromIndicies(listOfMessages, indicies):
    jsonParser = json.loads(json.dumps(listOfMessages))
    messages = jsonParser["messages"]
    msgs = []
    for message in messages:
        msgs.append(message["text"].encode('utf-8'))

    na = np.array(msgs)
    nb = np.array(indicies)
    out = list(na[nb])
    return out