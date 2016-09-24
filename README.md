# tweetindex-streamer

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
