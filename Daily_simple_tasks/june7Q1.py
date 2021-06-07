"""
1. Python Program to find largest element in an array
"""
def max(array):
    max=0
    for i in range(len(array)):
        if array[i]>array[max]:
            max=i
    return array[max]
            
    
    
if _name=='main_':
    array=[1,20,32,199,39,3000,2873]
    max=max(array)
    print("largest element in the array {array} is {max}".format(array=array,max=max))
"""
Output:
largest element in the array [1, 20, 32, 199, 39, 300, 2873] is 2873
***
largest element in the array [1, 20, 32, 199, 39, 3000, 2873] is 3000
"""
