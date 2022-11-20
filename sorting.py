# from app import MainWindow
from AscendingAlgos import *
import AscendingAlgos
from DescendingAlgos import *
class Sorting:
    
    
    @staticmethod
    
    def InsertionSort(array,type,index):
        print(index)
        start = 0
        end = len(array)
        # print(end)
        for i in range(start, end + 2 ):
            key = array[index][i]
            j = i - 1
            
            if type == 'ascend':
                while key < array[index][j] and j >= start: #backwards linear scan
                    array[index][j + 1] = array[index][j]
                    for k in range(0,8):
                        # if k == index:
                        #     continue
                        array[k][j + 1] ,array[k][j] = array[k][j] , array[k][j + 1]
                    # array[0][j + 1] = array[0][j]
                    # array[1][j + 1] = array[1][j]
                    # array[2][j + 1] = array[2][j]
                    # array[3][j + 1] = array[3][j]
                    # array[4][j + 1] = array[4][j]
                    # array[5][j + 1] = array[5][j]
                    # array[6][j + 1] = array[6][j]
                    # array[7][j + 1] = array[7][j]
                    j = j - 1
                
                array[index][j + 1] = key
            
            elif type == 'descend':
                while key > array[index][j] and j >= start: # j > = start beacuse we r sorting from start to end as desired by user
                    array[index][j + 1] = array[index][j]
                    for k in range(0,8):
                        # if k == index:
                        #     continue
                        array[k][j + 1] ,array[k][j] = array[k][j] , array[k][j + 1]
                    # array[0][j + 1] = array[0][j]
                    # array[1][j + 1] = array[1][j]
                    # array[2][j + 1] = array[2][j]
                    # array[3][j + 1] = array[3][j]
                    # array[4][j + 1] = array[4][j]
                    # array[5][j + 1] = array[5][j]
                    # array[6][j + 1] = array[6][j]
                    # array[7][j + 1] = array[7][j]
                    j = j - 1
                    
                array[index][j + 1] = key
        # print(array)
        return array
    @staticmethod
    def SelectionSort(array, type, index):
        if type == 'ascend':
            SelectionSort1(array[index], 0, len(array[index]) - 1, array)
        elif type == 'descend':
            SelectionSortDescending(array[index], 0, len(array[index]) - 1, array)
        return array
    @staticmethod
    def BubbleSort(array, type, index):
        if type == 'ascend':
            array[index] = BubbleSort1(array[index], 0, len(array[index]) - 1, array, index)
        elif type == 'descend':
            array[index] = BubbleSort2(array[index], 0, len(array[index]) - 1, array, index)
        return array

    @staticmethod
    def mergeSort(arr,type,index):
        copy = arr[index].copy()
        start = 0
        end = len(arr) - 1
        
        if type == 'ascend':
            MergeSortAscnding(arr[index] , start, end)
        elif type == 'descend':
            # end -= 1
            MergeSortDescending(arr[index] , start, end)
        # print(arr[index])
        # print(copy)
        
        for i in range(len(arr[index])):
            inx = copy.index(arr[index][i])
            
            
            for k in range(8):
                if k != index:
                    arr[k][inx] ,arr[k][i] = arr[k][i] , arr[k][inx]
        
        return arr
    
    @staticmethod
    def BubbleSortF(arr,type,index):
        copy = arr[index].copy()
        start = 0
        end = len(arr) - 1
        
        if type == 'ascend':
            arr[index] = BubbleSort(arr[index],start,end)
        elif type == 'descend':
            arr[index] = BubbleSort(arr[index],start,end)
            
        
        for i in range(len(arr[index])):
            inx = copy.index(arr[index][i])
            
            
            for k in range(8):
                if k != index:
                    arr[k][inx] ,arr[k][i] = arr[k][i] , arr[k][inx]
        return arr
    
    @staticmethod
    def TimSortF(arr,type,index):
        copy = arr[index].copy()
        start = 0
        end = len(arr)
        
        if type == 'ascend':
            arr[index] = TimSort(arr[index],start,end)
        elif type == 'descend':
            arr[index] = TimSortDescending(arr[index],start,end)
        
        
        for i in range(len(arr[index])):
            inx = copy.index(arr[index][i])
            
            
            for k in range(8):
                if k != index:
                    arr[k][inx] ,arr[k][i] = arr[k][i] , arr[k][inx]
        return arr 
    
    @staticmethod
    def HeapSortF(arr,type,index):
        # print(arr[index])
        copy = arr[index].copy()
        start = 0
        end = len(arr)
        
        if type == 'ascend':
            arr[index] = heap_sort(arr[index])
        elif type == 'descend':
            arr[index] = heap_sort_des(arr[index])
        
        
        for i in range(len(arr[index])):
            inx = copy.index(arr[index][i])
            
            
            for k in range(8):
                if k != index:
                    arr[k][inx] ,arr[k][i] = arr[k][i] , arr[k][inx]
        
        return arr 
    
    @staticmethod
    def ThreeWayMergeF(arr,type,index):
        # print(arr[index])
        copy = arr[index].copy()
        start = 1
        end = len(arr)
        
        # print(type(arr[index]))
        if type == 'ascend':
            arr[index] = merge_sort_3way(arr[index], start, end)
        elif type == 'descend':
            arr[index] = merge_sort_3way_des(arr[index], start, end)
        
        # print(arr[index])
        
        for i in range(len(arr[index])):
            inx = copy.index(arr[index][i])
            
            
            for k in range(8):
                if k != index:
                    arr[k][inx] ,arr[k][i] = arr[k][i] , arr[k][inx]
        
        return arr 
    
    @staticmethod
    def QuickSortF(arr,type,index):
        # print(arr[index])
        copy = arr[index].copy()
        start = 0
        end = len(arr)
        
        # print(type(arr[index]))
        if type == 'ascend':
            arr[index] = QuickSortAscending(arr[index], start, end)
        elif type == 'descend':
            arr[index] = QuickSortDescending(arr[index], start, end)
        
        # print(arr[index])
        
        for i in range(len(arr[index])):
            inx = copy.index(arr[index][i])
            
            
            for k in range(8):
                if k != index:
                    arr[k][inx] ,arr[k][i] = arr[k][i] , arr[k][inx]
        
        return arr
    
    @staticmethod
    def CocktailSortF(arr,type,index):
        # print(arr[index])
        copy = arr[index].copy()
        start = 0
        end = len(arr) - 1
        
        # print(type(arr[index]))
        if type == 'ascend':
            arr[index] = CocktailSortAsc(arr[index], start, end)
        elif type == 'descend':
            arr[index] = CocktailSortDes(arr[index], start, end)
        
        # print(arr[index])
        
        for i in range(len(arr[index])):
            inx = copy.index(arr[index][i])
            
            
            for k in range(8):
                if k != index:
                    arr[k][inx] ,arr[k][i] = arr[k][i] , arr[k][inx]
        
        return arr 

    @staticmethod
    def CountingSortF(arr,type,index):
        # print(arr[index])
        copy = arr[index].copy()
        
        # print(type(arr[index]))
        if type == 'ascend':
            arr[index] = CountingSort(arr[index])
        elif type == 'descend':
            arr[index] = CountingSortDescending(arr[index])
        
        # print(arr[index])
        
        for i in range(len(arr[index])):
            inx = copy.index(arr[index][i])
            
            
            for k in range(8):
                if k != index:
                    arr[k][inx] ,arr[k][i] = arr[k][i] , arr[k][inx]
        
        return arr 
    
    @staticmethod
    def RadixSortF(arr,type,index):
        # print(arr[index])
        copy = arr[index].copy()
        
        # print(type(arr[index]))
        if type == 'ascend':
            arr[index] = RadixSort(arr[index])
        elif type == 'descend':
            arr[index] = RadixSortDescending(arr[index])
        
        # print(arr[index])
        
        for i in range(len(arr[index])):
            inx = copy.index(arr[index][i])
            
            
            for k in range(8):
                if k != index:
                    arr[k][inx] ,arr[k][i] = arr[k][i] , arr[k][inx]
        
        return arr 
    @staticmethod
    def BucketSortF(arr,type,index):
        # print(arr[index])
        copy = arr[index].copy()
        max_el = max(arr[index])
        to_div = [arr[index][i] / max_el for i in range(len(arr[index]))]
                
        # print(type(arr[index]))
        if type == 'ascend':
            arr[index] = BucketSort(to_div)
        elif type == 'descend':
            arr[index] = BucketSortDescending(to_div)
        
        for i in range(len(arr[index])):
            inx = copy.index(arr[index][i])
            
            
            for k in range(8):
                if k != index:
                    arr[k][inx] ,arr[k][i] = arr[k][i] , arr[k][inx]
        
        return arr 
# array = [['Hamza', 'Shahzaib', 'Afraz'],[70, 49, 38],['A+', 'B+', 'C+']]


# print(Sorting.BubbleSort(array, 'descend', 1))
        