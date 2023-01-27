# program for pascal triangle

from math import factorial

rows = int(input("Enter the number of rows"))

for a in range(0,rows):
    print()
    for b in range(rows,a,-1):
        print(" ",end='')
    for c in range(0,a+1):
        print(factorial(a)// (factorial(c)*factorial(a-c)),end=" ")
            
    
