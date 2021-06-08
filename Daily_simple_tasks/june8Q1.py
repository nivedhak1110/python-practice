"""
1. Sort array of numbers. Any algorithm
# this program uses selection sort
->maintains a sorted subarray and an unsorted subarray
"""
def selection_sort(array):
    for i in range(len(array)):
        min_pos=i
        for j in range(i+1,len(array)):
            if array[min_pos]>array[j]:
                min_pos=j
        array[i],array[min_pos]=array[min_pos],array[i]   
    return array
    
if __name__=='__main__':
    array=[100,182,782,98,1,3,738,1000]
    print("Initial array:",array)
    sorted_array=selection_sort(array)
    print("selection sorted array:",sorted_array)
"""
Output:
Initial array: [100, 182, 782, 98, 1, 3, 738, 1000]
selection sorted array: [1, 3, 98, 100, 182, 738, 782, 1000]
"""
    
    
