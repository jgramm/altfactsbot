# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 11:12:33 2017

@author: James
"""

import tweepy #https://github.com/tweepy/tweepy
import csv
from secrets import *

def get_all_tweets(screen_name):
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)
    
    
    alltweets = []	
    new_tweets = api.user_timeline(screen_name = screen_name,count=20)
    alltweets.extend(new_tweets)
    
    oldest = alltweets[-1].id - 1
    
    
    
    while len(new_tweets) > 0:
        
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        
        alltweets.extend(new_tweets)
        
        oldest = alltweets[-1].id - 1
        
        outtweets = [[tweet.id_str, str(tweet.created_at), str(tweet.text.encode("utf-8"))] for tweet in alltweets]
        #outtweets = [tweet.text for tweet in alltweets]
        
    with open('%s_tweets.txt' % screen_name, 'w') as f:
        for tweet in outtweets:
            #writer = csv.writer(f)
            #writer.writerow(["id","created_at","text"])
            #writer.writerows(outtweets)
            
            print(tweet)
            f.write('\t'.join(tweet) + '\n')
            
            
            
if __name__ == '__main__':
    get_all_tweets('realDonaldTrump')