"""
Q-3
How to convert list to dictionary in Python
Method - 1 Using Dictionary Comprehension
dictionary comprehension syntax:
{key: value for (key, value) in iterable}
Method - 2 Using zip() function
"""
stud_name=["ram","raj","ravi","ramya"]
stud_mark=[90,80,65,89]
# Dictionary comprehension method:
dict1={key:"passed" for key in stud_name}
print(dict1)
# Zip method:
dict2={key:value for (key,value) in zip(stud_name,stud_mark)}
print(dict2)
"""
Output:
{'ram': 'passed', 'raj': 'passed', 'ravi': 'passed', 'ramya': 'passed'}
{'ram': 90, 'raj': 80, 'ravi': 65, 'ramya': 89}

"""
