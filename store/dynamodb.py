# -*- coding: utf-8 -*-

import json
import requests
import uuid

from settings import TWEETINDEX

def create_id(document):
    if not 'id' in document:
        document['id'] = str(uuid.uuid4())
    return document

def create_item(documents):
    for document in documents:
        document = create_id(document)
        print json.dumps(document)
        requests.post(TWEETINDEX['endpoint'], headers=TWEETINDEX['headers'], data=json.dumps(document))
    return True
