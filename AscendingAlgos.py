# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 13:21:00 2022

@author: Afraz Butt
"""

import random
import csv
import time
import math



def RandomArray(size): # This function is a basic and self-expalanatory
    array = []
    for i in range(size):
        rnd = random.randint(1, 100)
        rnd = math.ceil(rnd)
        array.append(rnd)
    return array

def InsertionSort(array,start,end):
    for i in range(start,end+1):
        key = array[i]
        j = i - 1
        
        while key < array[j] and j >= start: #backwards linear scan
            array[j + 1] = array[j]
            j = j - 1
        
        array[j + 1] = key
    return array

def BubbleSort(array,start,end):
  for i in range(len(array) - 1):
    for j in range(0, len(array) - i - 1):

      if array[j] > array[j + 1]:
            array[j] , array[j+1] = array[j+1],array[j]
        
    
    return array    

def BubbleSort1(array,start,end, array2D, index):
    for i in range(start,end + 1):
        for j in range(start ,end - i):
            if array[j + 1] < array[j]: #adjacent elements toRun
                array[j+1] , array[j] = array[j],array[j+1]
                for k in range(0,len(array2D)):
                    if k != index:
                        array2D[k][j + 1] ,array2D[k][j] = array2D[k][j] , array2D[k][j + 1]
                
    return array

def SelectionSort(array,start,end):
    for i in range(start,end+1):
        min_ind = i
        for j in range(i+1,end):
            if array[j] < array[min_ind]:
                min_ind = j
        (array[i], array[min_ind]) = (array[min_ind], array[i])
    
    return array
def SelectionSort1(array,start,end, array2D):
    for i in range(start,end):
        for j in range(i + 1 , end):
            if array[j] < array[i]: #minimum elements toRun
                array[j] , array[i] = array[i] , array[j]  
                for k in range(0,len(array2D)):
                    array2D[k][j + 1] ,array2D[k][j] = array2D[k][j] , array2D[k][j + 1]
                
    array[end] = array[end - 1]
    return array

def Merge(array,p,q,r):
    start = array[p : q + 1] 
    end = array[q + 1 : r + 1]
    
    start.append(math.inf) #sentinel variables
    end.append(math.inf)
    
    i = 0
    j = 0
    if type(start[0]) == str:
        for k in range(p,r + 1):
            if str(start[i]) < str(end[j]):
                array[k] = start[i]
                i = i  + 1
            else:
                array[k] = end[j]
                j = j  + 1
    else:
        for k in range(p,r + 1):
            if (start[i]) < (end[j]):
                array[k] = start[i]
                i = i  + 1
            else:
                array[k] = end[j]
                j = j  + 1
   
  
def MergeSortAscnding(A, p, r):
    if p < r:
        # return
        q = (p+r)//2
        MergeSortAscnding(A, p, q)
        MergeSortAscnding(A, q+1, r)
        Merge(A, p, q, r)
        return A

def TimSort(array,start,end):
    min_run = 70 #Blocks of smallest arrat dat is effeciently sorted using Insertion Sort
    n = len(array)

    for i in range(0,n,min_run):
        end = min((i + n - 1) , (n - 1))
        insertionSortTim(array,i,end)

    s = min_run
    while s < n:
        for j in range(0,n,s *2):
            mid = min((n - 1), (j + s - 1)) #merge function midpoint getting, n-1 is for when formula value exceeds array bounds
            if s < mid:
                Merge(array,start,mid,end)
        s = s * 2
    return array

def insertionSortTim(arr, start, end):
    for i in range(start + 1, end + 1):
        j = i
        while j > start and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

def CountingSort(A):
    maxA, minA = MaxElement(A), MinElement(A)
    C = [0] * ((maxA - minA) + 1)
    B = [0] * len(A)
    for i in range(0, len(A)):
        C[A[i] - minA] += 1
    for i in range(1, len(C)):
        C[i] += C[i-1]
    for i in range(len(A)-1, -1, -1):
        B[C[A[i] - minA] - 1] = A[i]
        C[A[i] - minA] -= 1
    return B

def BucketSort(A):
    C = []
    for i in range(0, len(A)):
        C.append([])
    for i in range(0, len(A)):
        intNumber = int(A[i] * int(len(A)))
        C[intNumber].append(A[i])
    for i in range(0, len(C)): # end + 1 because values are input as computerized manner
        C[i] = InsertionSort(C[i], 0, len(C[i]) - 1)
    k = 0
    for i in range(0, len(A)):
        for j in range(0, len(C[i])):
            A[k] = C[i][j]
            k += 1
    return A

def CocktailSortAsc(A, start, end):
    toRun = True
    while toRun == True:
        toRun = False
 
        # loop from left to right same as the bubble
        # sort
        for i in range(start, end):
            if (A[i] > A[i + 1]):
                A[i], A[i + 1] = A[i + 1], A[i]
                toRun = True
 
        
        if toRun == False:
            break
        toRun = False
        end = end-1
 
        for i in range(end-1, start-1, -1):
            if (A[i] > A[i + 1]):
                A[i], A[i + 1] = A[i + 1], A[i]
                toRun = True
 
        start = start + 1

    return A

def MaxElement(A):
    return max(A)

def MinElement(A):
    return min(A)

def Count_Sort_Radix(arr, d):
 
    n = len(arr)
    copy_sort = [0] * (n)
    
    counters = [0] * (10)
    
    for i in range(0, n):
        idx = arr[i] // d
        counters[idx % 10] += 1
    
    for i in range(1, 10):
        counters[i] += counters[i - 1]
    
    i = n - 1
    while i >= 0:
        idx = arr[i] // d
        copy_sort[counters[idx % 10] - 1] = arr[i]
        counters[idx % 10] -= 1
        i -= 1
 
    i = 0
    for i in range(0, len(arr)):
        arr[i] = copy_sort[i]

def RadixSort(A):
    max_element = max(A)
 
    radix = 1
    while max_element / radix >= 1:
        Count_Sort_Radix(A, radix)
        radix *= 10
    return A

def merge(arr, start, mid1, mid2, end):

    start_array = arr[start -1 : mid1]
    mid_array = arr[mid1: mid2 + 1]
    end_array = arr[mid2 + 1 : end]

    start_array.append(math.inf)
    mid_array.append(math.inf)
    end_array.append(math.inf)
    
    ind_start = 0
    ind_mid = 0
    ind_end = 0
    for i in range(start-1, end):
        minimum = min([start_array[ind_start], mid_array[ind_mid], end_array[ind_end]])
        if minimum == start_array[ind_start]:
            arr[i] = start_array[ind_start]
            ind_start += 1
        elif minimum == mid_array[ind_mid]:
            arr[i] = mid_array[ind_mid]
            ind_mid += 1
        else:
            arr[i] = end_array[ind_end]
            ind_end += 1
            
def merge_sort_3way(arr, start, end):

    if len(arr[start -1: end]) < 2:
        return arr
    else: 
        mid1 = start + ((end - start) // 3)
        mid2 = start + 2 * ((end-start) // 3)

        merge_sort_3way(arr, start, mid1)
        merge_sort_3way(arr, mid1+1, mid2 + 1)
        merge_sort_3way(arr, mid2+2, end)
        merge(arr, start, mid1, mid2, end)
        return arr
    


def parent(index):
    return index // 2

def start(index):
    return 2*index + 1

def end(index):
    return 2*index + 2

def max_heapify(array,index,n):
    l = start(index)
    r = end(index)
    # heap_size = len(array) 
    largest = index
    
    if l < n and array[l] > array[index]:
        largest = l
        
    
        
    if r < n and array[r] > array[largest]:
        largest = r
    
    
    if largest != index:
        (array[index] ,array[largest]) = (array[largest] , array[index])
        max_heapify(array,largest,n)

def build_max_heap(array):
    heap_size = len(array)
    
    for i in range(((heap_size // 2)), -1 , -1):
        max_heapify(array,i,heap_size)
    
    # print(array) #correct heap until now

def heap_sort(array):
    build_max_heap(array)
    n = len(array)
    
    # heap_size = n - 1
    # print('array before: ' + str(array))
    
    
    for i in range(n-1,0,-1):
        array[0] , array[i] = array[i] , array[0]
        
        
        # if heap_size > 0:
        # heap_size -= 1
        # print('heap size is: ' + str(heap_size))
        
        
        max_heapify(array,0,i) #i is to tell max heapify that it do its work uptil this limit
        
        
        # print(array)
    return array

# arr = [312,413,3,423,5,3,342,1,2,53]

# print (merge_sort_3way(arr,1,10))


# Arr = RandomArray(10)

# startTime = time.time()

# Arr = CountingSort(Arr)

# endTime = time.time()

# print(endTime - startTime)

# CocktailSort(Arr, 0, len(Arr))

# print(Arr)

# Arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
# print(Arr)

# Arr = BucketSort(Arr)

# print(Arr)
