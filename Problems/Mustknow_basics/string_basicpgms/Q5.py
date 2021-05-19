"""
Q-5 Differnt methods to concatenate strings in python
 String concatenation is a process when one string is merged 
 with another string. It can be done in the following ways.

1.Using + operators
2.Using join() method
3.Using format() function
4.Using % method
"""
str1=input("enter a string 1:")
str2=input("enter a string 2:")

#1.Using + operators
con1=str1+str2
print("1.Using + operator concatenated string {con1}".format(con1=con1))
#**************
#2.Using join() method
con2="".join([str1,str2])
print("2.Using join() method concatenated string {con2}".format(con2=con2))
#**************
#3.Using format method
print("3.Using format() method concatenated string {str1}{str2}".format(str1=str1,str2=str2))
#**************
#4.Using % method
print("4.Using modulo operator method concatenated string % s % s" % (str1,str2))  
"""
Output:
enter a string 1:hello
enter a string 2:world
1.Using + operator concatenated string helloworld
2.Using join() method concatenated string helloworld
3.Using format() method concatenated string helloworld
4.Using modulo operator method concatenated string hello world
"""
