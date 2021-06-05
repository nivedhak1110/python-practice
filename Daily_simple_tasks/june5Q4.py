"""
4.Prime number in between a range
Prime number:
a number that is divisible only by itself and by 1
examples:
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199...

"""
start=int(input("enter the start of the interval:"))
end=int(input("enter the end of the interval:"))
for i in range(start,end+1):
    temp=i
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count=count+1
    if count==2:
        print(temp)
"""
Output:
enter the start of the interval:1
enter the end of the interval:10
2
3
5
7
***
enter the start of the interval:1
enter the end of the interval:20
2
3
5
7
11
13
17
19
***
enter the start of the interval:50
enter the end of the interval:100
53
59
61
67
71
73
79
83
89
97
***
"""
