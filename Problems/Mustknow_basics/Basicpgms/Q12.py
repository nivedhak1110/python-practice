"""
Q12
Python Program to Print all Prime Numbers between an Interval
"""
start=int(input("enter start of interval: "))
end=int(input("enter end of interval: "))
count=0
for i in range(start,end+1):
    for j in range(1,i+1):
        if i%j==0:
            count=count+1
    if count==2:
        print(i)
    count=0  
"""
Output:
enter start of interval: 10
enter end of interval: 50
11
13
17
19
23
29
31
37
41
43
47
enter start of interval: 1
enter end of interval: 11
2
3
5
7
11
"""
