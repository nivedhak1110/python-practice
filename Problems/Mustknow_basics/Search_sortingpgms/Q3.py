"""
Q-3 selection Sort in Python
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.
1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.
"""
def selection_sort(array):
    
    for i in range(len(array)):
        min_index=i
        for j in range(i+1,len(array)):
            if array[min_index]>array[j]:
                min_index=j
        array[i],array[min_index]=array[min_index],array[i]#swap the elements in one line without using temporary variable
    return array            


if __name__=='__main__':
    array=[111,22,12,34,43,749,322,21,10,3]
    print("Initial unsorted array:",array)
    sorted_array=selection_sort(array)
    print("array sorted using selection sort:",sorted_array)

"""
Output:
Initial unsorted array: [111, 22, 12, 34, 43, 749, 322, 21, 10, 3]
array sorted using selection sort: [3, 10, 12, 21, 22, 34, 43, 111, 322, 749]
"""
