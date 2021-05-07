"""
Q-6 Move all zeros present in an array to the end

Input :  arr[] = {1, 2, 0, 4, 3, 0, 5, 0};
Output : arr[] = {1, 2, 4, 3, 5, 0, 0};

Input : arr[]  = {1, 2, 0, 0, 0, 3, 6};
Output : arr[] = {1, 2, 3, 6, 0, 0, 0};"""
def move_zeros_toend(array):
    count=0
    for i in range(len(array)):
        if(array[i]!=0):
            array[count]=array[i]
            count=count+1
    while count<len(array):
        array[count]=0
        count=count+1
    print("result",array)
    
if __name__=='__main__':
    array=[1, 2, 0, 0, 0, 3, 6]
    move_zeros_toend(array)
    
