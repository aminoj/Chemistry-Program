d_balanced = {1:['2 NaOH','H2SO4'], 2:['Na2SO4','2 H2O'], 
     3:['HCl','NaOH'], 4:['NaCl','H2O'], 
     5:['Ba(OH)2','2 HNO3'], 6:['Ba(NO3)2','2 H2O']}

 
print d_balanced[1][1][0]
print
print
counter = 0

while counter < 6:
    counter = counter+1
    print counter
    print d_balanced[counter][1][0]
    
    if d_balanced[counter][1][0].isdigit():
        print "okay"
        print
    else:
        print d_balanced[counter][1][0]
        print
