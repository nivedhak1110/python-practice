#Q-2Sort binary array in linear time
"""Input:  { 1, 0, 1, 0, 1, 0, 0, 1 }
 
  Output: { 0, 0, 0, 0, 1, 1, 1, 1 }
"""
"""
simple way is to count the number of zeros(m) and ones(n) and 
then fill first idices with m zeros next indices by n ones
 """
def binary_array_sort(array):
    m=array.count(0)#number of zeroes
    #print(m)
    n=array.count(1)#number of ones
    #print(n)
    arr=[]
    for i in range(m):
        arr.append(0)
    for i in range(n):
        arr.append(1)
    print("sorted binary array:",arr)
    return    
     
if __name__=='__main__':
    array=[1, 0, 1, 0, 1, 0, 0, 1 ]
    binary_array_sort(array)
"""output:
sorted binary array: [0, 0, 0, 0, 1, 1, 1, 1]
"""
