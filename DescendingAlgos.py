# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 19:24:36 2022

@author: SalmanTrader
"""
from AscendingAlgos import *
import random, math, sys
def RandomArrayForBucket(size): # This function is a basic and self-expalanatory
    array = []
    for i in range(size):
        rnd = random.randint(0, 9)
        rnd /= 10
# =============================================================================
#         rnd = math.ceil(rnd)
# =============================================================================
        array.append(rnd)
    return array

def RandomArray(size): # This function is a basic and self-expalanatory
    array = []
    for i in range(size):
        rnd = random.randint(1, 100)
        rnd = math.ceil(rnd)
        array.append(rnd)
    return array

def SelectionSortDescending(array,start,end, array2D):
    for i in range(start,end):
        for j in range(i + 1 , end):
            if array[j] > array[i]: #maximum elements swapped
                array[j] , array[i] = array[i] , array[j]  
                for k in range(0,3):
                    array2D[k][j + 1] ,array2D[k][j] = array2D[k][j] , array2D[k][j + 1]
                
    array[end] = array[end - 1]
    return array
def InsertionSortDescending(array, start, end):
    for i in range(start, end + 1): # end + 1 because values are input as computerized manner
        key = array[i]
        j = i - 1 # pointer variable
        while key > array[j] and j >= start: # j > = start beacuse we r sorting from start to end as desired by user
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
    return array
        
def MergeSortDescending(array, start, end):
    if start < end: # check for length of array not equal to 1
        q = (start + end) // 2   # // is used to convert answer to floor directly
        MergeSortDescending(array, start, q) # first half of array sliced recursively
        MergeSortDescending(array, q + 1, end)  # second half of array sliced recursively
        MergeDescending(array, start, q, end) 
   
        
def MergeDescending(array, p, q, r):
    n1 = q - p + 1  # counter variable to copy array
    n2 = r - q      # counter variable to copy array
    # L, R = [], []   # python initiallization
    # for i in range(0,n1):
    #     L.append(array[p+i]) # copying L side of array
    # for j in range(0,n2):
    #     R.append(array[q+j+1]) # copying right side of array
    L = array[p:q + 1]     # tried to lesser the total time by slicing but not worked properly
    R = array[q+1:r+1]
    L.append(-(math.inf))  # sys.maxize gives maximum integer we r using as a sentinel
    R.append(-(math.inf))
    
    if type(L[0]) == str:
        i, j = 0, 0
        for k in range(p, r + 1):
            if str(L[i]) >= str(R[j]):
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
    else:
        i, j = 0, 0
        for k in range(p, r + 1):
            if (L[i]) >= (R[j]):
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1

def BubbleSort2(array, start, end, array2D, index):
    for i in range(start,end + 1):
        for j in range(start, end - i):
            if array[j] < array[j + 1]:   # compairing alternate indexes
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp       # swaping
                for k in range(0,len(array2D[0])):
                    if k != index:
                        array2D[k][j + 1] ,array2D[k][j] = array2D[k][j] , array2D[k][j + 1]

def BubbleSortDes(array,start,end):
    for i in range(start,end + 1):
        for j in range(start ,end - i):
            if array[j + 1] >= array[j]: #adjacent elements swapped
                array[j+1] , array[j] = array[j],array[j+1]
                
    return array           
def mergeSortDescending(array , start, end):
    if len(array) > 1:

        
        r = len(array)//2
        Left = array[:r]
        Right = array[r:]

        
        mergeSortDescending(Left,start,end)
        mergeSortDescending(Right,start,end)

        i = j = k = 0

        
        while i < len(Left) and j < len(Right):
            if Left[i] > Right[j]:
                array[k] = Left[i]
                i += 1
            else:
                array[k] = Right[j]
                j += 1
            k += 1

       
        while i < len(Left):
            array[k] = Left[i]
            i += 1
            k += 1

        while j < len(Right):
            array[k] = Right[j]
            j += 1
            k += 1
         

def MergeSortAscending(array , start, end):
    if len(array) > 1:

        
        q = len(array)//2
        Left = array[start:q + 1]
        Right = array[q + 1:end + 1]

        
        MergeSortAscending(Left,start,end)
        MergeSortAscending(Right,start,end)

        i = j = k = 0

        
        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                array[k] = Left[i]
                i += 1
            else:
                array[k] = Right[j]
                j += 1
            k += 1

       
        while i < len(Left):
            array[k] = Left[i]
            i += 1
            k += 1

        while j < len(Right):
            array[k] = Right[j]
            j += 1
            k += 1

def TimSortDescending(array,start,end):
    min_run = 70 #Blocks of smallest array that is effeciently sorted using Insertion Sort
    n = len(array)

    for i in range(0,n,min_run):
        end = min((i + n - 1) , (n - 1))
        insertionSortTimDes(array,i,end)

    s = min_run
    while s < n:
        for j in range(0,n,s *2):
            mid = min((n - 1), (j + s - 1)) #merge function midpoint getting, n-1 is for when formula value exceeds array bounds
            if s < mid:
                MergeDescending(array,start,mid,end)
        s = s * 2
    return array

def insertionSortTimDes(arr, start, end):
    for i in range(start + 1, end + 1):
        j = i
        while j > start and arr[j] > arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1




def QuickSortAscending(A, p, r):
    if p < r:
        q = PartitionAscending(A, p, r)
        QuickSortAscending(A, p, q - 1)
        QuickSortAscending(A, q + 1, r)
        return A

def PartitionAscending(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def QuickSortDescending(A, p, r):
    if p < r:
        q = PartitionDescending(A, p, r)
        QuickSortDescending(A, p, q - 1)
        QuickSortDescending(A, q + 1, r)
        return A

def PartitionDescending(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] >= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

# Bucket Sort 

def BucketSortDescending(A):
    C = []
    for i in range(0, len(A)):
        C.append([])
    for i in range(0, len(A)):
        intNumber = int(A[i] * int(len(A)))
        C[intNumber].append(A[i])
    for i in range(0, len(C)): # end + 1 because values are input as computerized manner
        C[i] = InsertionSortDescending(C[i], 0, len(C[i]) - 1)
    k = 0
    for i in range(len(A) - 1, -1, -1):
        for j in range(0, len(C[i])):
            A[k] = C[i][j]
            k += 1
    return A

def CountingSortDescending(A):
    """Descending"""
    maxA, minA = MaxElement(A), MinElement(A)
    C = [0] * ((maxA - minA) + 1)
    B = [0] * len(A)
    for i in range(len(A)-1, -1, -1):
        C[A[i] - minA] += 1
    for i in range(len(C) - 1, 0, -1):
        C[i - 1] += C[i]
    for i in range(0, len(A)):
        B[C[A[i] - minA] - 1] = A[i]
        C[A[i] - minA] -= 1
    return B

def Count_Sort_Radix_descending(arr, d):
 
    n = len(arr)
    copy_sort = [0] * (n)
    counters = [0] * (10)
    
    for i in range(0, n):
        idx = arr[i] // d
        counters[idx % 10] += 1
    
    for i in range(1, 10):
        counters[i - 1] += counters[i]
 
    i = n - 1
    while i >= 0:
        # idx = arr[i] // d
        # print(idx)
        
        # # print(int(9-arr[i]/idx%10))
        # copy_sort[-counters[int(9-arr[i]/idx%10)]] = arr[i]
        # # counters[idx % 10] -= 1
        idx = arr[i] // d
        # print(counters[idx % 10] + 1)
        copy_sort[counters[idx % 10] + 1] = arr[i]
        counters[idx % 10] += 1
        # i -= 1
        i -= 1
 
    i = 0
    for i in range(0, len(arr)):
        arr[i] = copy_sort[i]

def RadixSortDescending(A):
    max_element = max(A)
 
    radix = 1
    while max_element / radix >= 1:
        Count_Sort_Radix_descending(A, radix)
        radix *= 10
    return A


def MaxElement(A):
    return max(A)

def MinElement(A):
    return min(A)

def CocktailSortDes(A, start, end):
    toRun = True
    end -= 1
    while toRun == True:
        toRun = False
        for i in range(start, end):
            if A[i] < A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                toRun = True
        if toRun == False:
            end -= 1
        for i in range(end - 1, start - 1, -1):
            if A[i] < A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                toRun = True
        start += 1
    return A


def left(index):
    return 2*index + 1

def right(index):
    return 2*index + 2

def min_heapify(array,index,n):
    l = left(index)
    r = right(index)
    # heap_size = len(array) 
    smallest = index
    
    if l < n and array[l] < array[smallest]:
        smallest = l
        
    
        
    if r < n and array[r] < array[smallest]:
        smallest = r
    
    
    if smallest != index:
        (array[index] ,array[smallest]) = (array[smallest] , array[index])
        min_heapify(array,smallest,n)

def build_min_heap(array):
    heap_size = len(array)
    
    for i in range(((heap_size // 2)), -1 , -1):
        min_heapify(array,i,heap_size)
    
    # print(array) #correct heap until now

def heap_sort_des(array):
    build_min_heap(array)
    n = len(array)
    
    # heap_size = n - 1
    # print('array before: ' + str(array))
    
    
    for i in range(n-1,0,-1):
        array[0] , array[i] = array[i] , array[0]
        
        
        # if heap_size > 0:
        # heap_size -= 1
        # print('heap size is: ' + str(heap_size))
        
        
        min_heapify(array,0,i) #i is to tell max heapify that it do its work uptil this limit
        
        
        # print(array)
    return array


def merge_3_des(arr, start, mid1, mid2, end):

    start_array = arr[start -1 : mid1]
    mid_array = arr[mid1: mid2 + 1]
    end_array = arr[mid2 + 1 : end]

    start_array.append(-math.inf)
    mid_array.append(-math.inf)
    end_array.append(-math.inf)
    
    ind_start = 0
    ind_mid = 0
    ind_end = 0
    for i in range(start-1, end):
        maximum = max([start_array[ind_start], mid_array[ind_mid], end_array[ind_end]])
        if maximum == start_array[ind_start]:
            arr[i] = start_array[ind_start]
            ind_start += 1
        elif maximum == mid_array[ind_mid]:
            arr[i] = mid_array[ind_mid]
            ind_mid += 1
        else:
            arr[i] = end_array[ind_end]
            ind_end += 1
            
def merge_sort_3way_des(arr, start, end):

    if len(arr[start -1: end]) < 2:
        return arr
    else: 
        mid1 = start + ((end - start) // 3)
        mid2 = start + 2 * ((end-start) // 3)

        merge_sort_3way_des(arr, start, mid1)
        merge_sort_3way_des(arr, mid1+1, mid2 + 1)
        merge_sort_3way_des(arr, mid2+2, end)
        merge_3_des(arr, start, mid1, mid2, end)
        return arr
    
