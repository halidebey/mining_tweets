from tweepy import OAuthHandler, API, Stream
from tweepy.streaming import StreamListener
import codecs
import json
import datetime

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

count=0

f = codecs.open('twitter.txt',encoding='utf-8', mode='w+')

class TwitterListener ( StreamListener ):

    def on_tweet ( self, data ):

        global count
        count = count + 1

        tweet = json.loads(data)

        username = tweet['user']['screen_name'] 
        body     = tweet['text'] 
        hashtags = tweet['entities']['hashtags'] 
        date     = tweet['created_at'] 

        f.write ( data + username + body + hashtags + '\n' )

        if count == 2:
            return False
        else:
            return True
    
    def on_error ( self, status ):
        print ( status )


if __name__ == '__main__':

    auth     = OAuthHandler ( CONSUMER_KEY, CONSUMER_SECRET )
    api      = API ( auth ) 
    listener = TwitterListener ( api )
    stream   = Stream ( auth, listener)

    auth.set_access_token ( ACCESS_TOKEN, ACCESS_TOKEN_SECRET )
    words_to_track = [ 'revolut' ]
    stream.filter ( track=words_to_track )

    f.close()