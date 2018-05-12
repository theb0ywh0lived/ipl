#Import the necessary methods from tweepy library
from tweepy import Stream
import pandas as pd
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
#Variables that contain the user credentials to access Twitter API
#(Note: replace with your own values from https://apps.twitter.com/)
consumer_key="consumer key"
consumer_secret="consumer secret"
author_token="author token"
author_secret="author secret"
class listener(StreamListener):
#This is a basic listener that just prints received tweets
    def on_data(self, data):
        try:
     #writing data to file
            savefile = open('tweetDBcars.csv','a')
            savefile.write(data)
            savefile.close()
            return(True)
        except BaseException as e:
            print ('failed ondata',str(e))
            time.sleep(5)
def on_error(self, status):
        print (status)
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(author_token, author_secret)
twitterStream = Stream(auth, listener())
# getting tweets that have any of these words
twitterStream.filter(track=['car' 
 'chevy','ford','toyota',
    'acura','kia','audi',
    'chrystler','dodge','ferrari'
    'fiat','buick','cadillac','chevrolet',
    'bmw','honda','jeep','lexus','mazda',
    'mini','nissan','tesla''volvo','saab','porshe'])
tweets_data_path = 'tweetDBcars.csv'
tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
tweets = pd.DataFrame()
index = 0
for num, line in enumerate(tweets_data):
  try:
     print (num,line['text'])
     tweets.loc[index,'text'] = line['text']
     index = index + 1 
  except:
     print (num, "line not parsed")
     continue 
def brand_in_tweet(brand, tweet):
    brand = brand.lower()
    tweet = tweet.lower()
    match = re.search(brand, tweet)
    if match:
        print ('Match Found')
        return brand
    else:
        print ('Match not found')
        return 'none'
from textblob import TextBlob
for index, row in tweets.iterrows():
    temp = TextBlob(row['text'])
    tweets.loc[index,'sentscore'] = temp.sentiment.polarity    
for column in tweets.columns:
    for idx in tweets[column].index:
        x = tweets.get_value(idx,column)
        try:
            x = unicode(x.encode('utf-8','ignore'),errors ='ignore')          
            if type(x) == unicode:
                unicode(str(x),errors='ignore')
            else: 
                df.set_value(idx,column,x)
        except Exception:
            print ('encoding error: {0} {1}'.format(idx,column))
            tweets.set_value(idx,column,'')
            continue
tweets.to_csv('tweets_export.csv')                   