import networkx as nx
import numpy as np

from nltk.tokenize.punkt import PunktSentenceTokenizer
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer


def textrank(document):
    sentence_tokenizer = PunktSentenceTokenizer()
    sentences = sentence_tokenizer.tokenize(document)

    bow_matrix = CountVectorizer().fit_transform(sentences)
    normalized = TfidfTransformer().fit_transform(bow_matrix)

    similarity_graph = normalized * normalized.T

    nx_graph = nx.from_scipy_sparse_matrix(similarity_graph)
    scores = nx.pagerank(nx_graph)
    return sorted(((scores[i], s) for i, s in enumerate(sentences)),
                  reverse=True)

def getFileData(fname):
    arr = []
    f = open(fname, "r")
    for line in f:
        arr.append(line)
    return arr


fname = "data.txt"
messages = getFileData(fname)


document = ""
for message in messages:
    document += message + " "

# document_0 = "The discovery and archaeological study of Chandraketugarh, 35 kilometres (22 mi) north of Kolkata, provide evidence that the region in which the city stands has been inhabited for over two millennia.[22][23] Kolkata's recorded history began in 1690 with the arrival of the English East India Company, which was consolidating its trade business in Bengal. Job Charnock, an administrator who worked for the company, was formerly credited as the founder of the city;[24] In response to a public petition,[25] the Calcutta High Court ruled in 2003 that the city does not have a founder.[26] The area occupied by the present-day city encompassed three villages: Kalikata, Gobindapur, and Sutanuti. Kalikata was a fishing village; Sutanuti was a riverside weavers' village. They were part of an estate belonging to the Mughal emperor; the jagirdari (a land grant bestowed by a king on his noblemen) taxation rights to the villages were held by the Sabarna Roy Choudhury family of landowners, or zamindars. These rights were transferred to the East India Company in 1698"

results = textrank(document)
