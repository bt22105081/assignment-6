# three no sum equal zero

l = [3,5,-8,5,6,-11]

for a in range(0,len(l)-1) :
    for b in range(0,len(l)-1):
        if(-(l[a]+l[b]) in l):
            print(l[a],l[b],-(l[a]+l[b]))
        else:
            continue


        
