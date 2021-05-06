#Q-4Find majority element -Boyer–Moore Majority Vote Algorithm
"""
************
Defenition:
A majority element in an array A[] of size n is an element 
that appears more than n/2 times (and hence there is at most 
one such element).
*************
Input : {3, 3, 4, 2, 4, 4, 2, 4, 4}
Output : 4
Explanation: The frequency of 4 is 5 which is greater
than the half of the size of the array size. 

Input : {3, 3, 4, 2, 4, 4, 2, 4}
Output : No Majority Element
Explanation: There is no element whose frequency is
greater than the half of the size of the array size.
"""
"""
def majority(array):
    half_arr_length=len(array)//2
    for i in range(len(array)):
        n=array[i]
        countof_element=array.count(n)
        if countof_element > half_arr_length:
            print("Majority Element",n)
            return
    print("No Majority Element")
            
            
        

if __name__=='__main__':
    array=[3, 3, 4, 2, 4, 4, 2, 4,4]
    majority(array)
output:
Majority Element 4
"""
def majority(array):
    half_arr_length=len(array)//2
    
    for i in range(len(array)):
        n=array[i]
        #print(n)
        countof_element=0
        for j in range(len(array)):
            
            if array[j]==n:
                countof_element=countof_element+1
        #print(countof_element)
                
        if countof_element > half_arr_length:
            print("Majority Element",n)
            return
            
    print("No Majority Element")
if __name__=='__main__':
    array=[3, 3, 4, 2, 4, 4, 2, 4,4]
    majority(array)
    
