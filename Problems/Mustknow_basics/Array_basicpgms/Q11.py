"""
Q-11
Python program to print the sum of all elements in an array
"""
array=[1,2,3,4,5]
sum=0
for i in range(len(array)):
    sum=sum+array[i]
print("sum of all elements in this array is {sum}".format(sum=sum))
"""
Output:
sum of all elements in this array is 15
"""
