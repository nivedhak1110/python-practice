"""
2.palindrome string using recursion
example:
dad,mom,malayalam,madam
"""
def reverse_string(string,rev,i):
    if i==-1:
        return rev
    else:
        rev=rev+string[i]
        i=i-1
        #print("{string},{rev},{i}".format(string=string,rev=rev,i=i))
        return reverse_string(string,rev,i)
    
    
if __name__=='__main__':
    string=input("enter a string:")
    temp=string
    rev=""
    length=len(string)
    i=length-1
    reverse_string=reverse_string(string,rev,i)
    print("reverse_string:",reverse_string)
    if(temp==reverse_string):
        print("{temp} is a palindrome string".format(temp=temp) )
    else:
        print("{temp} is not a palindrome string".format(temp=temp) )
"""
Output:
enter a string:malayalam
reverse_string: malayalam
malayalam is a palindrome string
******
enter a string:python
reverse_string: nohtyp
python is not a palindrome string
******
enter a string:mom
reverse_string: mom
mom is a palindrome string
"""
