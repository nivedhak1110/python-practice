#Q-30Equilateral triangle pattern of characters/alphabets
"""
Pattern: –
            A  
           B C  
          D E F  
         G H I J  
        K L M N O  
       P Q R S T U  
      V W X Y Z [ \ 
                    """
#program
n=int(input("enter the number of rows:"))
asci_value=65
m=(2*n)-2
for i in range(1,n+1):
    for j in range(1,m+1):
        print(end=" ")
    m=m-1
    for j in range(i):
        char=chr(asci_value)
        print(char,end=" ")
        asci_value=asci_value+1
    print()
 """
 output:
 enter the number of rows:7
            A 
           B C 
          D E F 
         G H I J 
        K L M N O 
       P Q R S T U 
      V W X Y Z [ \  """
