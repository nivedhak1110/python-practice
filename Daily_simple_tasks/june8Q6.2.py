"""
Python Program to find second largest element in an array(without sorting)
#method 2
"""
def max(array):
    max=0
    for i in range(len(array)):
        if array[i]>array[max]:
            max=i
    return array[max]
            
def second_max(array,max):
    sec_max=0
    for i in range(len(array)):
        if array[i]>array[sec_max] and array[i]<max:
            sec_max=i
    return sec_max
    
if __name__=='__main__':
    array=[1,20,32,199,39,3000,28731]
    max=max(array)
    print("largest element in the array {array} is {max}".format(array=array,max=max))
    second_max=second_max(array,max)
    print("second largest element in the array {array} is {second_max}".format(array=array,second_max=array[second_max]))
    
"""
Output:
largest element in the array [1, 20, 32, 199, 39, 3000, 2873] is 3000
second largest element in the array [1, 20, 32, 199, 39, 3000, 2873] is 2873

*****
largest element in the array [1, 20, 32, 199, 39, 3000, 28731] is 28731
second largest element in the array [1, 20, 32, 199, 39, 3000, 28731] is 3000

"""
