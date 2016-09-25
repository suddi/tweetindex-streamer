# -*- coding: utf-8 -*-

from store.dynamodb import create_item

def on_error(status_code):
    item = {
        'type': 'error',
        'status': status_code
    }

    create_item([item])
    return True
