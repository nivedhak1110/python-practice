"""
3.Prime number or not
Prime number:
a number that is divisible only by itself and by 1
examples:
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97...

"""
num=int(input("enter a number:"))
count=0
for i in range(1,num+1):
    if num%i==0:
        count=count+1
#print("count:",count)
if count==2:
    print("{num} is a prime number".format(num=num))
else:
    print("{num} is not a prime number".format(num=num))
    
"""
Output:
enter a number:2
2 is a prime number
****
enter a number:10
10 is not a prime number
****
enter a number:11
11 is a prime number
****
enter a number:97
97 is a prime number
"""
