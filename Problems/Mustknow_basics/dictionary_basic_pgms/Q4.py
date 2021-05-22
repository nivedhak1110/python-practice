"""
Q-4
Merge two Dictionaries in Python
"""
dict1={
    "ram":32,
    "ravi":43,
    "ramya":29
}
dict2={
    "preethi":32,
    "prakash":43,
    "primya":29
}
print("Dict1:",dict1)
print("Dict2:",dict2)
dict3={}
print("Dict3 before merging Dict1,Dict2:",dict3)
dict3=dict1
print("Dict3 before merging with Dict2:",dict3)
for (k,v) in dict2.items():
    dict3[k]=v
print("Dict3 after merging dict1,dict2:",dict3)
"""
Output:
Dict1: {'ram': 32, 'ravi': 43, 'ramya': 29}
Dict2: {'preethi': 32, 'prakash': 43, 'primya': 29}
Dict3 before merging Dict1,Dict2: {}
Dict3 before merging with Dict2: {'ram': 32, 'ravi': 43, 'ramya': 29}
Dict3 after merging dict1,dict2: {'ram': 32, 'ravi': 43, 'ramya': 29, 'preethi': 32, 'prakash': 43, 'primya': 29}
"""
