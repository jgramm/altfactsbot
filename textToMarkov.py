# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 15:35:37 2017

@author: James
"""
import re
import random


def textTo2GramMarkov(text, wordsTo=dict(), count=0):
    
    #text = re.sub(r'\W+', '', text)
    #words = text.split()
    words = "".join((char if char.isalpha() else " ") for char in text).split()
    
    # wordsTo is a dictionary of dictionaries. The first key is the word we are
    # going to markov from. The second key is the word we are going to. The 
    # value is the frequency of key1 to key2
    
    for i in range(len(words) - 1):
        
        w = words[i]
        w1 = words[i+1]

        if w in wordsTo.keys():
            
            if w1 in wordsTo[w].keys():
                wordsTo[w][w1] += 1            
            else:
                wordsTo[w][w1] = 1
            
        else:
            wordsTo[w] = {w1: 1}
    
            
    return (wordsTo, count + len(words) - 1)
    
    
def allTextTo2GramMarkov(lines):

    wordsTo = dict()   
    count = 0
    count2 = 0
    
    for line in lines:
        print('finished %i of %i' % (count2, len(lines)))   
        count2 += 1
        (wordsTo, tempCount) = textTo2GramMarkov(line.lower(), wordsTo)
        count += tempCount
    
    #wordsTo = normalize2GramMarkov(wordsTo, count)
    
    print('done generating markov')
    print(wordsTo)
    return wordsTo


def sampleMarkov(markov, w):
    if w in markov.keys():
        probs = markov[w]
        
        total = 0
        for val in probs.values():
            total += val
        
        ind = random.randrange(total)
        
        for key in probs.keys():
            ind -= probs[key]
            if ind <= 0:
                
                return key
            
    return 'oops'


#def normalize2GramMarkov(markov, count):
#    for k1 in markov.keys():
#        for k2 in markov[k1].keys():
#            markov[k1][k2] /= count


def textTo3GramMarkov(text, wordsTo=dict()):
    
    #text = re.sub(r'\W+', '', text)
    #words = text.split()
    words = "".join((char if char.isalpha() else " ") for char in text).split()
    
    # wordsTo is a dictionary of dictionaries. The first key is the word we are
    # going to markov from. The second key is the word we are going to. The 
    # value is the frequency of key1 to key2
    
    for i in range(len(words) - 2):
        
        w = words[i]
        w1 = words[i+1]
        w2 = words[i+2]

        if w in wordsTo.keys():
            
            if (w1,w2) in wordsTo[w].keys():
                wordsTo[w][(w1,w2)] += 1            
            else:
                wordsTo[w][(w1,w2)] = 1
            
        else:
            wordsTo[w] = {(w1,w2): 1}
    
            
    return wordsTo

def allTextTo3GramMarkov(lines):

    wordsTo = dict()   
    count2 = 0
    
    for line in lines:
        print('finished %i of %i' % (count2, len(lines)))   
        count2 += 1
        wordsTo = textTo3GramMarkov(line.lower(), wordsTo)
        
    
    print('done generating markov')
    print(wordsTo)
    return wordsTo




def textTo3GramMarkov2(text, wordsTo=dict()):
    
    #text = re.sub(r'\W+', '', text)
    #words = text.split()
    words = "".join((char if char.isalpha() else " ") for char in text).split()
    
    # wordsTo is a dictionary of dictionaries. The first key is the word we are
    # going to markov from. The second key is the word we are going to. The 
    # value is the frequency of key1 to key2
    if len(words) < 3:
        return wordsTo
        
        
    for i in range(len(words) - 2):
        
        w = words[i]
        w1 = words[i+1]
        w2 = words[i+2]

        if w in wordsTo.keys():
            
            if w2 in wordsTo[(w,w1)].keys():
                wordsTo[(w,w1)][w2] += 1            
            else:
                wordsTo[(w,w1)][w2] = 1
            
        else:
            wordsTo[(w,w1)] = {w2: 1}
    
            
    return wordsTo

def allTextTo3GramMarkov2(lines):

    wordsTo = dict()   
    count2 = 0
    
    for line in lines:
        print('finished %i of %i' % (count2, len(lines)))   
        count2 += 1
        wordsTo = textTo3GramMarkov2(line.lower(), wordsTo)
        
    
    print('done generating markov')
    print(wordsTo)
    return wordsTo
 

def sample3Markov2(markov, w, w1):
    if (w,w1) in markov.keys():
        probs = markov[(w,w1)]
        
        total = 0
        for val in probs.values():
            total += val
        
        ind = random.randrange(total)
        
        for key in probs.keys():
            ind -= probs[key]
            if ind <= 0:
                
                return key
            
    return 'oops'           
           
           
           
def main():
    lines = []
    with open('trumpSpeeches.txt', 'r', encoding='UTF8') as f:
        lines = f.readlines()
    
    m = allTextTo3GramMarkov2(lines)

    w = 'build'
    w1 = 'a'
    
    print(w)
    for i in range(100):
        print(w1)
        s = sample3Markov2(m, w, w1)
        w = w1
        w1 = s
        
    #print(sampleMarkov(m,'warned'))
    


if __name__=='__main__':
    main()    