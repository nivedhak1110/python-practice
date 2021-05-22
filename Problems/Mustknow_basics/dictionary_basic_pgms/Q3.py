"""
Q-2  assignment operations on  Dictionaries in Python

dict1={}
dict1["key"]="value"-->to dictionary assignment
print(dict1)
output-->{'key': 'value'}
"""
#assignment in dictionary
student={}
student["ram"]=67
print(student)
student["ravi"]=88
print(student)
#update a value in dictionary
student["ravi"]=98# dictionary doesnot allow duplicates, mutable
print(student)
# find value for a particular key
print("value for a key ravi: ",student["ravi"])
#some dictionary important methods
print(student.keys())#returns list of dictionary keys
print(student.items())# returns list of tuple for each key value pair
"""
Output:
{'ram': 67}
{'ram': 67, 'ravi': 88}
{'ram': 67, 'ravi': 98}
value for a key ravi:  98
dict_keys(['ram', 'ravi'])
dict_items([('ram', 67), ('ravi', 98)])
"""
