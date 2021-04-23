#Q-31 Pattern of same character
"""
Pattern:

V 
V V 
V V V 
V V V V 
V V V V V 
"""
char=input("enter a character: ")
#char=V     
n=int(input("enter the number of rows: "))
for i in range(1,n+1):
    for j in range(i):
        print(char,end=" ")
    print()
""" 
Output:
enter a character: V
enter the number of rows: 5
V 
V V 
V V V 
V V V V 
V V V V V 
"""
