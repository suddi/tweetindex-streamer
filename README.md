# tweetindex-streamer

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a5c2b4b2016e40d4a9b55991d3cdab9f)](https://www.codacy.com/app/suddir/tweetindex-streamer?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=suddi/tweetindex-streamer&amp;utm_campaign=Badge_Grade)
[![license](https://img.shields.io/github/license/suddi/tweetindex-streamer.svg?maxAge=2592000)](git@github.com:suddi/tweetindex-streamer.git)

A stock tweet streamer using tweetstreamer and Twitter's Streaming API to collect market sentiment information based on Twitter users' tweets

## Install

````
pip install -r requirements.txt
````

## Usage

````
cp settings.py.TEMPLATE settings.py
````

Set the CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY and ACCESS_SECRET values

````
python main.py
````

This will start the process to stream tweets
