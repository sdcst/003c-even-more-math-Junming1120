#!python3

"""
Write a program to ask the user to input a length in centimeters. Convert this into feet and inches.  Round your inches to the nearest whole inch.
You will likely need to make use of at least one of the following:
* % modulus
* math.floor()

Sample output:
```
Enter a length in centimeters: 172
172 centimeters is 5 feet and 8 inches

Enter a length in centimeters: 32
32 centimeters is 1 feet and 1 inches
```
"""
import math 
c = float(input("enter a length in cm:"))
i = c/2.54
f = i/12
f = math.floor(f)
I = i-(12*f)
I = round(I)
print(f"{c}centimeters is {f} feet and {I}inches")

