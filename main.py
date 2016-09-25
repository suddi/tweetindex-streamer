# -*- coding: utf-8 -*-

from tweetstreamer import auth, listen
from settings import TWITTER, STOCK_CODES
from handlers.on_status import on_status
from handlers.on_error import on_error
from handlers.on_timeout import on_timeout
from handlers.on_disconnect import on_disconnect

def controller():
    connection = auth(TWITTER['consumer_key'], TWITTER['consumer_secret'], TWITTER['access_key'], TWITTER['access_secret'])
    listen(connection, STOCK_CODES.keys(), on_status, on_error, on_timeout, on_disconnect)


if __name__ == '__main__':
    controller()
