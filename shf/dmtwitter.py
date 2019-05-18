from dmsuper import DMSuper
import tweepy
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
from algo import phraseFreq
from myhtml import text_from_html
import sys

class DMTwitter(DMSuper):
    
    def getWeight(self):
        
        return .1
    
    def read(self):
        
        consumer_key = 'IstZYPCHpHJ0tNqhK2pH0muwY'
        consumer_secret = 'Abn2jZU9OGc8EgsGmP0B25QQKGnNdImqd8nGWghJH9yHU7w1tU'
        access_token = '575219980-ObVuWJxSjVyEfDjpG2NdMtTlpo3uH0X1qEFpKhH3'
        access_token_secret = 'DBKyTiEKtxx70h0H3cMZnh27oe6PA9QT2jNiTrMkeycqJ'
        
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        
        api = tweepy.API(auth)
        
        '''public_tweets = api.home_timeline()
        for tweet in public_tweets:
            print(tweet.text)'''
            
        account_list = ['GuyAdami',
                        'karenfinerman',
                        'grassosteve',
                        'BKBrianKelly',
                        'petenajarian',
                        'DavidSeaburg',
                        'timseymour',
                        'jimcramer',
                        'realDonaldTrump',
                        'CNBCJosh',
                        'StockTwits',
                        'Benzinga'
                        ]
        '''if (len(sys.argv) > 1):
            account_list = sys.argv[1:]
        else:
            print("Please provide a list of usernames at the command line.")
            sys.exit(0)'''
        
        if len(account_list) > 0:
            for target in account_list:
                item = api.get_user(target)
                print("User: " + item.name)
                #print("screen_name: " + item.screen_name)
                #print("description: " + item.description)
                #print("statuses_count: " + str(item.statuses_count))
                #print("friends_count: " + str(item.friends_count))
                #print("followers_count: " + str(item.followers_count))
                
                tweets = item.statuses_count
                account_created_date = item.created_at
                delta = datetime.utcnow() - account_created_date
                account_age_days = delta.days
                #print("Account age (in days): " + str(account_age_days))
                if account_age_days > 0:
                  print("Average tweets per day: " + "%.2f"%(float(tweets)/float(account_age_days)))
                
                hashtags = []
                mentions = []
                tweet_count = 0
                end_date = datetime.utcnow() - timedelta(days=1)
                culm = self.totals
                for status in Cursor(api.user_timeline, id=target).items(2):
                    print('Tweet: ')
                    print(status.text)
                    totals = phraseFreq(status.text)
                    culm[0] += totals[0]
                    culm[1] += totals[1]
                    print(totals)
                    tweet_count += 1
                    if hasattr(status, "entities"):
                        entities = status.entities
                        if "hashtags" in entities:
                            for ent in entities["hashtags"]:
                                if ent is not None:
                                    if "text" in ent:
                                        hashtag = ent["text"]
                                        if hashtag is not None:
                                            hashtags.append(hashtag)
                        if "user_mentions" in entities:
                            for ent in entities["user_mentions"]:
                                if ent is not None:
                                    if "screen_name" in ent:
                                        name = ent["screen_name"]
                                        if name is not None:
                                            mentions.append(name)
                    if status.created_at < end_date:
                        break
                print('Totals: ' + str(culm))
                print("Most mentioned Twitter users:")
                for item, count in Counter(mentions).most_common(10):
                  print(item + "\t" + str(count))
             
                print("Most used hashtags:")
                for item, count in Counter(hashtags).most_common(10):
                  print(item + "\t" + str(count))
             
                print("Processed " + str(tweet_count) + " tweets.")
                print('**************')
