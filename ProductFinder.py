d = {1:['NaOH','H2SO4'], 2:['Na2SO4','H2O'], 
     3:['HCl','NaOH'], 4:['NaCl','H2O'], 
     5:['Ba(OH)2','2HNO3'], 6:['Ba(NO3)2','H2O']}

product = ''
substance = 'NaOH'
array = ['HCl']
array.append(substance)
x = True
counter = 0

while x is True:
    counter=counter+1
            
    if array == d[counter]:
        product = d[counter+1]
        x = False
        print 'YAY'
    else:
        product = 'no reaction'
    
print product
