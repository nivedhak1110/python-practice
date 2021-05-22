"""
Q-1
create a dictionary
-->direct method ,using dict()method
"""
#method1
student={
    "ram":83,
    "raj":56,
    "ravi":90
}
print(type(student))
print(student)
# method 2 using the dict() method  
teacher=dict({"ramya":"CSE","primya":"ECE","suresh":"CSE"})
print(teacher)
# method 3 with each item in list as a key value pair
teacher_age=dict([("suresh",35),("ramya",30),("primya",29)])
print(teacher_age)
"""
Output:
<class 'dict'>
{'ram': 83, 'raj': 56, 'ravi': 90}
{'ramya': 'CSE', 'primya': 'ECE', 'suresh': 'CSE'}
{'suresh': 35, 'ramya': 30, 'primya': 29}
"""
