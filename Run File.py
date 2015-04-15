import ChemistryProject as cp

print 'Welcome to Titration Lab Simulator'
print 
print 'The following are the reactions available:'
print
print '1   -    NaOH(aq) and H2SO4(aq)'  
print '2   -    HCl(aq) and NaOH(aq)' 
print '3   -    Ba(OH)2(aq) and HNO3(aq)'
print
print 'Please notice that all subsances are in aqeous form. So both volume and molarity is expected. '
print 
d = cp.Beaker()
substance1 = raw_input('Enter your first compound: ')
amount1 = raw_input('Enter the amount in mL of the aqeous substance: ')
molarity1 = raw_input('Enter the molarity of this solution: ')

amount1 = float(amount1)
molarity1 = float(molarity1)

d.add(substance1, amount1, molarity1)

print
d.inside()
print

substance2 = raw_input('Enter your second compound: ')
amount2 = raw_input('Enter the amount in mL of the aqeous substance: ')
molarity2 = raw_input('Enter the molarity of this solution: ')

amount2 = float(amount2)
molarity2 = float(molarity2)

d.add(substance2, amount2, molarity2)
print
d.inside()
print
print 'COMPLETE DATA - ' 
d.outcome()
