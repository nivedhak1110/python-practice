"""
Q-2
How to convert list to dictionary in Python
#methods:dictionary comprehension,zip function
"""
vegetables=["tomato","potato","brinjal","caroot","beetroot"]
#no pair for beetroot in price so zip function removes it 
price=[50,60,40,30]
dict1={k:v for (k,v) in list(zip(vegetables,price)) }
print(dict1)

"""
Output:
{'tomato': 50, 'potato': 60, 'brinjal': 40, 'caroot': 30}
"""
