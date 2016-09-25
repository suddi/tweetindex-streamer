# -*- coding: utf-8 -*-

from store.dynamodb import create_item

def on_disconnect(error):
    item = {
        'type': 'disconnect',
        'status': error.message
    }

    create_item([item])
    return True
