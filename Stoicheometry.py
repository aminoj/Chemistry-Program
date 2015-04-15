from __future__ import division

d = {1:['NaOH','H2SO4'], 2:['Na2SO4','H2O'], 
     3:['HCl','NaOH'], 4:['NaCl','H2O'], 
     5:['Ba(OH)2','HNO3'], 6:['Ba(NO3)2','H2O']}

d_balanced = {1:['2 NaOH','H2SO4'], 2:['Na2SO4','2 H2O'], 
     3:['HCl','NaOH'], 4:['NaCl','H2O'], 
     5:['Ba(OH)2','2 HNO3'], 6:['Ba(NO3)2','2 H2O']}

array = ['NaOH','H2SO4']

amount = 32
molarity = 2

amount1 = 12
molarity1 = 4

totVolume = (amount+amount1)/1000

#-------------------------------------------------------------------------------
#limiting reactant

x = True 
counter = 0
            
while x is True:
    counter=counter+1
            
    if array == d[counter]:
        x = False
        
        if d_balanced[counter][0][0].isdigit():
             s_coeff= int(d_balanced[counter][0][0])
        else:
            s_coeff = 1     
             
        if d_balanced[counter][1][0].isdigit():
             s1_coeff= int(d_balanced[counter][1][0])
        else:
             s1_coeff = 1
             
moles = (amount*(molarity/1000))
print moles
moles1 = (amount1*(molarity1/1000))
print moles1

testing = moles/s_coeff
testing1 = moles1/s1_coeff

if testing > testing1:
    limitReact = d[counter][1]
    limitReactNum = moles1
    s_coeff = s1_coeff
    
elif testing1 > testing:
    limitReact = d[counter][0]
    limitReactNum = moles
    s1_coeff = s_coeff
    
else:
    limitReact = "Both are Limiting Reactants"    
    limitReactNum = moles
    
print limitReact
print limitReactNum

#-------------------------------------------------------------------------------
#finding moles of products

if d_balanced[counter+1][0][0].isdigit():
    s_product_coeff= int(d_balanced[counter+1][0][0])
else:
    s_product_coeff = 1     
             
if d_balanced[counter+1][1][0].isdigit():
    s1_product_coeff= int(d_balanced[counter+1][1][0])
else:
    s1_product_coeff = 1

molesOfProd = ((s_product_coeff)/(s_coeff))*limitReactNum
molesOfProd1 = ((s1_product_coeff)/(s_coeff))*limitReactNum

#-------------------------------------------------------------------------------
#Results

molarity = molesOfProd/totVolume
molarity1 =  molesOfProd1/totVolume

print molarity
print molarity1
    
