"""
5. Python program to find second largest number in a list
# logic used in this program--->sort the list in descending order then find the second largest element
"""
def desc_sort(array):
    for i in range(len(array)):
        max_pos=i
        for j in range(i+1,len(array)):
            if array[j]>array[max_pos]:
                max_pos=j
        array[i],array[max_pos]=array[max_pos],array[i]
    return array
        
if __name__=='__main__':
    array=[-1,3,4,2,10,212,100,102]
    print("Initial Array:",array)
    desc_sort=desc_sort(array)
    print("array sorted in descending order:",desc_sort)
    second_largest=desc_sort[1]
    print("{second_largest} is the second largest element  in the array {array}".format(second_largest=second_largest,array=array))
"""
Output:
Initial Array: [-1, 3, 4, 2, 10, 212, 100, 102]
array sorted in descending order: [212, 102, 100, 10, 4, 3, 2, -1]
102 is the second largest element  in the array [212, 102, 100, 10, 4, 3, 2, -1]
"""
