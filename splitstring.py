# split a string at hyphens and print alphabetical order

n=input("enter the string: ") 
l=n.split('-') 
l.sort() 
print('-'.join(l))
