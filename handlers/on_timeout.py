# -*- coding: utf-8 -*-

from store.dynamodb import create_item

def on_timeout():
    item = {
        'type': 'timeout',
        'status': 'timed out'
    }

    create_item([item])
    return True
