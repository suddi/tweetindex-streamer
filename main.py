# -*- coding: utf-8 -*-

from datetime import datetime

from tweetstreamer import auth, listen
from settings import (
    CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET,
    STOCK_CODES, BUY_SENTIMENT
)

def generate_list(values):
    list_item = []
    for value in values:
        if 'text' in value.keys():
            list_item.append(value['text'])
        elif 'screen_name' in value.keys():
            list_item.append(value['screen_name'])
    return list_item

def on_status(status):
    text = status.text.lower()
    buy_sentiment = None
    sentiment_word = []
    for word, sentiment in BUY_SENTIMENT.iteritems():
        if word in text and not buy_sentiment:
            buy_sentiment = sentiment
            sentiment_word.append(word)

    if buy_sentiment != None:
        stocks = generate_list(status.entities['symbols'])
        hashtags = generate_list(status.entities['hashtags'])
        user_mentions = generate_list(status.entities['user_mentions'])

        item = {
            '_id'           : status.id,
            'screen_name'   : status.user.screen_name,
            'full_name'     : status.user.name,
            'location'      : status.user.location,
            'stock'         : stocks,
            'num_stock'     : len(stocks),
            'tweet'         : status.text,
            'buy_sentiment' : buy_sentiment,
            'sentiment_word': sentiment_word,
            'favorited'     : status.favorite_count,
            'retweeted'     : status.retweet_count,
            'is_retweet'    : status.retweeted,
            'hashtags'      : hashtags,
            'user_mentions' : user_mentions,
            'geo'           : status.geo,
            'coordinates'   : status.coordinates,
            'created_at'    : status.created_at,
            'timestamp'     : datetime.utcnow()
        }

        print item

    return True

def on_error(status_code):
        item = {
            'status'    : status_code,
            'timestamp' : datetime.utcnow()
        }

        return True

def on_timeout():
    item = {
        'status'    : 'timed out',
        'timestamp' : datetime.utcnow()
    }

    return True

def on_disconnect(error):
    item = {
        'status': error.message,
        'timestamp': datetime.utcnow()
    }


def controller():
    connection = auth(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
    listen(connection, STOCK_CODES.keys(), on_status, on_error, on_timeout, on_disconnect)


if __name__ == '__main__':
    controller()
