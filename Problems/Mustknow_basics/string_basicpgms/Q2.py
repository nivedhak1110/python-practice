"""
Q-2
Python Program to Remove Punctuation from a String
"""
string=input("Enter a string:")
punctuation='''''!()-[]{};:'"\,<>./?@#$%^&*_~'''
no_punctuation_string=""
for char in string:
    if char not in punctuation:
        no_punctuation_string=no_punctuation_string+char
print(" string without punctuation")
print(no_punctuation_string)
"""
Output:
Enter a string:Enter a string:iam nivedha, from "cbe".
string without punctuation
iam nivedha from cbe
"""
