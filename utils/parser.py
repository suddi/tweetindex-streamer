# -*- coding: utf-8 -*-

from settings import BUY_SENTIMENT

def parse_sentiment(text):
    sentiment_words = []
    overall_sentiment = 0
    for word, sentiment in BUY_SENTIMENT.iteritems():
        if word in text:
            sentiment_words.append(word)
            if sentiment:
                overall_sentiment += 1
            else:
                overall_sentiment -= 1

    buy_sentiment = None
    if (overall_sentiment > 0):
        buy_sentiment = 'buy'
    elif (overall_sentiment < 0):
        buy_sentiment = 'sell'

    return {
        'words': sentiment_words,
        'buy_sentiment': buy_sentiment
    }
