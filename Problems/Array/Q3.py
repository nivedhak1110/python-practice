#Q-3Find the maximum product of two integers in an array
"""
given an integer array {-10, -3, 5, 6, -2}
output,the maximum product  is the (-10, -3) or (5, 6) pair
"""
"""
consider every pair of elements and update
the maximum product if required
"""
import sys
def maximum_product(array):
    max= -sys.maxsize#maxsize attribute of the sys module fetches the largest value a variable of data type can store
    max_i = max_j = -1
    for i in range(len(array)-1):
        for j in range(i+1,len(array)-1):
            if array[i]*array[j]>max:
                max=array[i]*array[j]
                max_i=i
                max_j=j
    print("Maximum product pair:",(array[max_i],array[max_j]))
    print("product:",max)
            

     
if __name__=='__main__':
    array=[-10, -3, 5, 6, -2]
    maximum_product(array)
"""
Output:
Maximum product pair: (-10, -3)
product: 30
"""
