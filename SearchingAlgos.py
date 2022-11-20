# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 21:07:37 2022

@author: SalmanTrader
"""

import math

from DescendingAlgos import *
from AscendingAlgos import *
def StartsWith(Arr, string, listt):
    """Arr is 1D array according to which search is to occur, array2D is complete list"""
    length = len(str(string))
    
    feed_back = [[],[],[],[],[],[],[],[]]
    
    for i in range(0, len(Arr)):
        if Arr[i][0:length] == string:
            ind = i
            feed_back[0].append(listt[0][ind])
            feed_back[1].append(listt[1][ind]) 
            feed_back[2].append(listt[2][ind]) 
            feed_back[3].append(listt[3][ind])
            feed_back[4].append(listt[4][ind])
            feed_back[5].append(listt[5][ind])
            feed_back[6].append(listt[6][ind])
            feed_back[7].append(listt[7][ind])
    # print(feedBack)
    # print(feed_back)
    return feed_back

def EndsWith(Arr, string, listt):
    """Arr[index] as input"""
    length = len(str(string))
    
    
    # print(Arr)
    feed_back = [[],[],[],[],[],[],[],[]]
    
    for i in range(0, len(Arr)):
        print(Arr[i][len(Arr[i]) - length:] + ' is comparing with ' + string)
        if string in Arr[i][len(Arr[i]) - length:]:
            
            ind = i
            feed_back[0].append(listt[0][ind])
            feed_back[1].append(listt[1][ind]) 
            feed_back[2].append(listt[2][ind]) 
            feed_back[3].append(listt[3][ind])
            feed_back[4].append(listt[4][ind])
            feed_back[5].append(listt[5][ind])
            feed_back[6].append(listt[6][ind])
            feed_back[7].append(listt[7][ind])
    return feed_back

def Contains(Arr, string,listt):
    """Arr[index] as input 1D Array, listt is 2D array"""
    length = len(string)
    
    feed_back = [[],[],[],[],[],[],[],[]]
    
    for i in range(0, len(Arr)):
        for j in range(0, len(Arr[i])):
            if Arr[j: j + length] == string:
                print(Arr[j: j + length])
                ind = i
                feed_back[0].append(listt[0][ind])
                feed_back[1].append(listt[1][ind]) 
                feed_back[2].append(listt[2][ind]) 
                feed_back[3].append(listt[3][ind])
                feed_back[4].append(listt[4][ind])
                feed_back[5].append(listt[5][ind])
                feed_back[6].append(listt[6][ind])
                feed_back[7].append(listt[7][ind])
                break
    return feed_back

def And(Arr, string,Arr2d):
    return Contains(Arr, string,Arr2d)

def Not(Arr, string,listt):
    """Arr[index] as input"""
    length = len(string)
    
    feed_back = [[],[],[],[],[],[],[],[]]
    
    for i in range(0, len(Arr)):
        check = False
        for j in range(0, len(Arr[i])):
            if Arr[i][j: j + length] == string:
                check = True
                break
        if check == False:
           ind = i
           feed_back[0].append(listt[0][ind])
           feed_back[1].append(listt[1][ind]) 
           feed_back[2].append(listt[2][ind]) 
           feed_back[3].append(listt[3][ind])
           feed_back[4].append(listt[4][ind])
           feed_back[5].append(listt[5][ind])
           feed_back[6].append(listt[6][ind])
           feed_back[7].append(listt[7][ind])
    return feed_back


# Numbers Searching Algos

def JumpSearch(Arr, number):
    
    n = math.sqrt(len(Arr))
    
    previous = 0
    
    while Arr[int(min(n, len(Arr) - 1))] < number:
        previous = n
        n += math.sqrt(len(Arr))
        if previous >= len(Arr):
            return -1
    
    while Arr[int(previous)] < number:
        previous += 1
        
        if previous == min(n, len(Arr)):
            return -1
    if Arr[int(previous)] == number:
        return previous
    return -1

def BinarySearchRecursive(Arr, number, low, high):
    if high >= low:
        mid = (low + (high)) // 2
        if Arr[mid] == number:
            return mid
        else:
            if str(Arr[mid]) < str(number):
                return BinarySearchRecursive(Arr, number, mid + 1, high)
            else:
                return BinarySearchRecursive(Arr, number, low, mid - 1)
    else:
        return False
    
def BinarySearch(Arr, number):
    low, high = 0, len(Arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if Arr[mid] == number:
            return True
        else:
            if Arr[mid] > number:
                high -= 1
            else:
                low += 1
    return False

def linearSearchStrings(arr,pattern,idx):
    """Linear Search Algorithm for strings"""
    feedBack = []
    for item in arr:
        if pattern in item[idx]:
            feedBack.append(item)
    
    return feedBack

def linearSearch(arr,Number,idx):
    """Linear Search Algorithm for Integers"""
    feedBack = []
    for item in arr:
        if item[idx] == Number:
            feedBack.append(item)
    
    return feedBack



def checkName(list,index,pattern):
    """String Matching Algorithm for names"""
    feed_back = [[],[],[],[],[],[],[],[]]
    NO_OF_ASCII = 256
    PRIME = 7351
    i = 0
    for item in list[index]:
        item = str(item)
        checker = rabinKarpMatcher(item , pattern,NO_OF_ASCII,PRIME)
        # print(checker)
        if checker is True:
            ind = i
            # print(list[3][ind])
            
            feed_back[0].append(list[0][ind])
            feed_back[1].append(list[1][ind]) 
            feed_back[2].append(list[2][ind]) 
            feed_back[3].append(list[3][ind])
            feed_back[4].append(list[4][ind])
            feed_back[5].append(list[5][ind])
            feed_back[6].append(list[6][ind])
            feed_back[7].append(list[7][ind])
        i += 1
    
    # print(feed_back[0])
    return feed_back
        

def rabinKarpMatcher(Text, Pattern, d, q):
    n = len(Text)
    m = len(Pattern)
    h = (pow(d, m-1)) % q  # hash function
    p = 0  # hash of text
    t = 0  # hash of pattern

    if len(Pattern) > len(Text):  # check for abnormal case
        return False

    # calculate hash for window (size equal to length of pattern) and pattern
    for i in range(m):
        p = ((d*p) + ord(Pattern[i])) % q
        t = ((d*t) + ord(Text[i])) % q

    for s in range(n-m+1):  # Rabin-Karp Loop, linear execution

        checker = 0
        if p == t:  # Check if both pattern and text hash to same value, then and only then
                    # check the sub-string one by one. This is to avoid spurious hits.
            for j in range(m):
                if Text[s+j] != Pattern[j]:
                    break
                else:
                    j += 1
                    checker += 1

            if checker == m:
                return True

        # shifting the left most (significant) digit to one place right by reassigning hash value 
        if s < n-m:
            t = (d*(t-ord(Text[s])*h) + ord(Text[s+m])) % q
            
            if t < 0:      #For negative values, increment them
                t = t + q
    
    return False

