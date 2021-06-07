"""
2. Python Program to find least element in an array
"""
def min(array):
    min=0
    for i in range(len(array)):
        if array[i]<array[min]:
            min=i
    return array[min]
            
    
    
if __name__=='__main__':
    array=[200,320,199,39,3000,2873]
    min=min(array)
    print("smallest element in the array {array} is {min}".format(array=array,min=min))
"""
Output:
smallest element in the array [1, 20, 32, 199, 39, 3000, 2873] is 1
*****
smallest element in the array [200, 320, 199, 39, 3000, 2873] is 39
"""
