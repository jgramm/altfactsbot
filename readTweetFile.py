# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 14:24:00 2017

@author: James
"""

def readTweets(fileName):
    
    tweets = []    
    with open(fileName, 'r') as f:

        for line in f:        
            tweet = {}
            seps = line.split('\t')
            tweet['text'] = seps[2]
            tweet['time'] = seps[1]
            tweet['id'] = seps[0]
            tweets.append(tweet)
    
    return tweets
        
        
        
if __name__=='__main__':
    print(readTweets('realDonaldTrump_tweets.txt'))