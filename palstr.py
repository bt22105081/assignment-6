# palindrome string

s = input("enter the string")
s1 = s.replace(" ","")
srev = ""
for a in range(len(s1)-1,-1,-1):
    srev = srev + s1[a]

if(s1 == srev):
    print("The string is a palindrome")
else:
    print("String is not palindrome")
    
