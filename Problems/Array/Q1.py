#Q-1 Find a (first) pair with the given sum in an array
#Given an unsorted array
def find_pair(array,sum):
    for i in range(len(array)-1):
        for j in range(i+1,len(array)-1):
            
            if array[i]+array[j]==sum:
                print("found pair with given sum",(array[i],array[j]))
                return # remove if all pairs required
    # No pair with the given sum exists in the list
    print("Pair not found")
    
if __name__== '__main__':
    sum=10
    array=[7,3,8,2,6,4,1]
    find_pair(array,sum)
    
#output
#found pair with given sum (7, 3)
