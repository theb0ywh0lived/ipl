#Import the necessary methods from tweepy library
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
#Variables that contain the user credentials to access Twitter API
#(Note: replace with your own values from https://apps.twitter.com/)
consumer_key = 'ILXgtJL3aqC0BuXXQDQnqMt8j'
consumer_secret = 'ATRYvAPXWxXHlIBmCzzAr0PIUYM1FRzYl2Vn6kPfJCQrndPThP'

access_token =  '2527556648-gKyjCVsMeInUAC3VmMltS5yUQFiK3fjY53FhsEn'
access_token_secret = 'hmuhYQ9r5fP5Ypq8yly5NnAuq3yoph8yPwFdCxnDtwq1L'
class listener(StreamListener):
#This is a basic listener that just prints received tweets
def on_data(self, data):
   try:
     #writing data to file
     saveFile = open('tweetDBcars.csv','a')
     saveFile.write(data)
     saveFile.close()
     return(True)
   except BaseException, e:
     print 'failed ondata,',str(e)
     time.sleep(5)
def on_error(self, status):
        print status
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
