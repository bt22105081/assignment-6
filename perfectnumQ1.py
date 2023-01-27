# program to find perfect numbers
n =  int(input("Enter the number to be checked : "))
sum = 0
for a in range(1,n+1):
    if(n%a == 0):
        sum = sum + a
    else:
        continue

if(sum == 0):
    print("no positive divisor")
elif((sum/2) == n):
    print(n," is a perfect number")
else:
    print(n," is not a perfect number")
