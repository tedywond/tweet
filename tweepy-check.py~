import tweepy
from tweepy import OAuthHandler

consumer_key = 'gakk5RzCm3yyxFhYCk8DG9ILG'
consumer_secret = 'S7scP5rxncnhFO0OqlvCzDOmq1aqeK5CNB7HkHWonr5AKAVGMf'
access_token = '3069335090-rbRqMKEILkiawbS7sqQdKB3C6bpW5A7bvh3Jhu3'
access_secret = 'njMK25O7Iow7rBI2igZ5V4rJxNfnpSsp3YBqxKGvqFNWJ'

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)

# for status in tweepy.Cursor(api.home_timeline).items(10):
# 	print(status._json, '\n')

# for friend in tweepy.Cursor(api.friends).items(10):
# 	print(friend._json) #returns dictionary 

# for tweet in tweepy.Cursor(api.user_timeline).items():
# 	print(tweet._json)

from tweepy.streaming import StreamListener
from tweepy import Stream

class MyListener(StreamListener):
	"""docstring for MyListener"""
	def on_data(self,data):
		try:
			with open('trend.json','a') as f:
				f.write(data)
				return True
		except BaseException as e:
			print('&quot;Error on_data: %s&quote;',str(e))
		return True

	def on_error(self,status):
		print(status)
		return True
		
twitter_stream = Stream(auth,MyListener())
twitter_stream.filter(track=["#obama"])