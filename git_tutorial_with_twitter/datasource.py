import tweepy

consumer_key = 'zzveO2grLcAL45BwJHmw'
consumer_secret = 'OAsz4gYXgqF9wl9M9iV8EszKeM0rtZS4BlRBXfMW88'
access_token = '318339423-jigs1sUQXWHMDHW8K8LNkdDktc3SOErevhFyb6Dw'
access_token_secret = 'Wl3ZC97BQJXSTkrxtY4GxjEUsGifQkjhLjxaumQdA'

class TweetList:
    def __init__(self, tweets):
        self.tweets = tweets

    def next(self):
        self.index += 1
        if(self.index == len(self.tweets)):
            raise StopIteration
        return self.tweets[self.index].text
        
    def __iter__(self):
        self.index = -1
        return self

def timeline(screenName):
    api = getAPI()
    tweets = api.user_timeline(screen_name=screenName)
    return TweetList(tweets)

def favorites(screenName):
    api = getAPI()
    user = api.get_user(screen_name=screenName)
    tweets = api.favorites(id=user.id)
    return TweetList(tweets)

def getAPI():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth_handler=auth)

    return api

if __name__ == "__main__":
    import os
    flask_env = os.environ.get("FLASK_ENV")
    if(flask_env == "DEVELOP"):
        SCREEN_NAME = "_junpei"
        print "result of timeline(%s)" % (SCREEN_NAME)
        for text in timeline(SCREEN_NAME):
            print text
        print "result of favorites(%s)" % (SCREEN_NAME)
        for text in favorites(SCREEN_NAME):
            print text
