"""
Q-1
Python Program to Sort Words in Alphabetic Order
Sorting:

Sorting is a process of arrangement. It arranges data 
systematically in a particular format. It follows some 
algorithm to sort data.
"""
string=input("enter a string:")
print("string in lower case:")
string=string.lower()
print(string)
print("list of words in the entered string:")
words=string.split()
print(words)
#sort
print("sorted list of words in the entered string:")
words.sort()
print(words)
"""
Output:
enter a string:iam nivedha FRom coimBatore
string in lower case:
iam nivedha from coimbatore
list of words in the entered string:
['iam', 'nivedha', 'from', 'coimbatore']
sorted list of words in the entered string:
['coimbatore', 'from', 'iam', 'nivedha']
"""
