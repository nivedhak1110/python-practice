"""
1.pallindrome number using recursion
palindrome number examples:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202,....
"""
def rev(n,sum):
    if(n==0):
        return sum
    else:
        sum=(sum*10)+(n%10)
        n=n//10
        return rev(n,sum)
    
if __name__=='__main__':
    n=int(input("enter a number:"))
    sum=0
    temp=n
    rev=rev(n,sum)
    print("reversed number:",rev)
    if(temp==rev):
        print("{temp} is a palindrome number".format(temp=temp))
    else:
        print("{temp} is  not a palindrome number".format(temp=temp))
"""
 Output:
enter a number:1234
reversed number: 4321
1234 is  not a palindrome number
*****
enter a number:1221
reversed number: 1221
1221 is a palindrome number
*****
enter a number:44
reversed number: 44
44 is a palindrome number
"""
