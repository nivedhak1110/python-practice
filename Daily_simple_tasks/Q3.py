"""
Pallindrome string
example:
madam,mam,dad,malayalam
"""
string=input("enter a string:")
temp=string
#print(temp)
str_len=len(string)
#print(str_len)
reverse_string=""
for i in range(str_len-1,-1,-1):
    reverse_string=reverse_string+string[i]
print("reverse_string:",reverse_string)
if(temp==reverse_string):
    print("{temp} is a palindrome string".format(temp=temp))
else:
    print("{temp} is not a palindrome string".format(temp=temp))
"""
Output:
***
enter a string:hello
reverse_string: olleh
hello is not a palindrome string
***
enter a string:malayalam
reverse_string:malayalam
malayalam is a palindrome string
***
enter a string:hello world
reverse_string:dlrow olleh
hello world is not a palindrome string
"""
