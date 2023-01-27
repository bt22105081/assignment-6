# pangrams

s = input("Enter the word or sentence")
lalpha = ['a','b','c','d','e','f','g','h','i','j'
          ,'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
c1 = 0
for i in lalpha:
    for j in s:
        c0 = 0
        if((i == j) or(i.upper() ==j)):
            c0+=1
            break
        else:
            continue
    if(c0 > 0):
        c1+=1
        continue

if(c1 ==26):
    print("Yes it is a pangram")
else:
    print("Not a pangram")
    
            
    
    
