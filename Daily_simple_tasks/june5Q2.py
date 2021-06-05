"""
2. Armstrong number between a range

A positive integer is called an Armstrong number of order n if
abcd... = a power n + b power n + c power n + d power n + ...
example:
1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474, 54748, ...

"""
start=int(input("enter the start of the range:"))
end=int(input("enter the end of the range:"))
for i in range(start,end+1):
    temp=i
    count=0
    if i==0:
        count=1
    else:
        while i>0:
            count=count+1
            i=i//10
    num=temp
    rem=0
    add=0
    while num>0:
        rem=num%10
        add=add+(rem**count)
        num=num//10
    if(temp==add):
        print(temp)
        
"""
Output:
enter the start of the range:100
enter the end of the range:1000
153
370
371
407
*****
enter the start of the range:500
enter the end of the range:10000
1634
8208
9474

"""
