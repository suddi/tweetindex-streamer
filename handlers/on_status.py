# -*- coding: utf-8 -*-

from store.dynamodb import create_item
from utils.parser import parse_sentiment

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
    sentiment = parse_sentiment(text)

    if sentiment['buy_sentiment']:
        items = []
        stocks = generate_list(status.entities['symbols'])
        hashtags = generate_list(status.entities['hashtags'])
        user_mentions = generate_list(status.entities['user_mentions'])

        for stock in stocks:
            item = {}
            item['tweet_id'] = str(status.id)
            item['type'] = 'tweet'
            if status.user.screen_name:
                item['screen_name'] = status.user.screen_name
            if status.user.name:
                item['full_name'] = status.user.name
            if status.user.location:
                item['location'] = status.user.location
            item['stock'] = stock
            item['tweet'] = status.text
            item['sentiment'] = sentiment['buy_sentiment']
            item['sentiment_words'] = sentiment['words']
            if status.favorite_count:
                item['favorited'] = status.favorite_count
            if status.retweet_count:
                item['retweeted'] = status.retweet_count
            if status.retweeted:
                item['is_retweet'] = status.retweeted
            item['hashtags'] = hashtags
            item['user_mentions'] = user_mentions
            if status.geo:
                item['geo'] = status.geo
            if status.coordinates:
                item['coordinates'] = status.coordinates
            item['created_at'] = status.created_at.strftime('%Y-%m-%dT%H:%M:%SZ')
            items.append(item)

        create_item(items)
    return True
