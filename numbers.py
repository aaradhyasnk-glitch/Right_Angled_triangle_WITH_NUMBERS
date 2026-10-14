a=1
for row in range (1,11,1):
    for column in range (1,16,1):
        if column<=row:
            print (a, end = " ")
            a= a+1
    print ( )
    
