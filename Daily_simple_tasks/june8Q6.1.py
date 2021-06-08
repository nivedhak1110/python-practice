"""
6.1find second largest element in an array without using sort
#method 1 most efficient method
"""
def max(array):
    max = 0
    max2 = 0
    for i in range(len(array)):
        if array[i] > array[max]:
            max = i
        elif array[i] > array[max2]:
            max2 = i
    return array[max], array[max2]


if __name__== "__main__":
    array = [1, 20, 32, 5000, 199, 39, 3000, 2900, 2873]
    max1, max2 = max(array)
    print("first max "+ str(max1))
    print("second max "+str(max2))
"""
Output:
first max 5000
second max 3000
"""
