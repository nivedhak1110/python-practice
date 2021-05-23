"""
Q-4
 Insertion sort in python
"""
def insertion_sort(array):
    for i in range(1,len(array)):#i=0 is considered as sorted initially,1 is inserted first
        value=array[i]#inserted value
        for j in range(i-1,-1,-1):
            if value<array[j]:
                array[j+1]=array[j]#shift to array[j] right
                array[j]=value#shift value to left
                #value,array[j]=array[j],value#wrong-->donot swap
    print("Insertion sorted array:",array)

if __name__=='__main__':
    array=[100,34,22,43,35,65,543,200,1222]
    print("Initial array:",array)
    insertion_sort(array)
"""
Output:
Initial array: [100, 34, 22, 43, 35, 65, 543, 200, 1222]
Insertion sorted array: [22, 34, 35, 43, 65, 100, 200, 543, 1222]
*****
Flow of execution:
Initial array: [100, 34, 22, 43, 35, 65, 543, 200, 1222]
Insertion sorted array: [34, 100, 22, 43, 35, 65, 543, 200, 1222]#1 index  element(34) is inserted and placed at correct  position
Insertion sorted array: [22, 34, 100, 43, 35, 65, 543, 200, 1222]
Insertion sorted array: [22, 34, 43, 100, 35, 65, 543, 200, 1222]
Insertion sorted array: [22, 34, 35, 43, 100, 65, 543, 200, 1222]
Insertion sorted array: [22, 34, 35, 43, 65, 100, 543, 200, 1222]
Insertion sorted array: [22, 34, 35, 43, 65, 100, 543, 200, 1222]
Insertion sorted array: [22, 34, 35, 43, 65, 100, 200, 543, 1222]
Insertion sorted array: [22, 34, 35, 43, 65, 100, 200, 543, 1222]


"""
