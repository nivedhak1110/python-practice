# Q-28 character pattern program 1
""" 
A  
B C  
D E F  
G H I J  
K L M N O  
P Q R S T U  
V W X Y Z [ \  """
n=int(input("enter the number of rows:"))
asci_value=65
for i in range(1,n+1):
    for j in range(i):
        char=chr(asci_value)#chr()--->asci to char
                            #ord()--->char to asci
        print(char,end=" ")
        asci_value=asci_value+1
    print()
        
