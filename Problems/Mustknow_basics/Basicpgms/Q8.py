"""
Q-8
Python program to convert Celsius to Fahrenheit
and Fahrenheit to Celsius
T(℉) = T(℃) x 9/5 + 32
Or,

T(℉) = T(℃) x 1.8 + 32
t(c)=(t(f)-32)/1.8
"""
tempc=float(input("enter temperature in celsius:"))
tempf=tempc*1.8+32
print("temperature in fahrenheit:%0.3f" %tempf)
tempf=float(input("enter temperature in fahrenheit:"))
tempc=(tempf-32)/1.8
print("temperature in celcious:%0.3f"%tempc)
"""
Output:
enter temperature in celsius:37
temperature in fahrenheit:98.600
enter temperature in fahrenheit:98.600
temperature in celcious:37.000"""
