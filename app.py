import tweepy
import time

auth = tweepy.OAuthHandler('DC2CafVgKapteW2M0oevT5GAq', 'ySKfUJ3cYTEiFDBTsV8gAOHLktcheSmvsj528VUSbTfqywrGvG')
auth.set_access_token('1317765409508970496-FPBBYybTrVwNQ95z27YkyUUie4x7a8', '2oV2p5U0AS7KezhgnautzJr2RmqYHnAVf6jzCXytNFEmw')

api = tweepy.API(auth)
while True:
  user = api.get_user('OmSuneel')
  f = user.followers_count
  api.update_profile(name=f'OmSuneel {f} Followers')
  print(f'OmSuneel {f} Followers')
  time.sleep(60)
  
