from __future__ import division

class Beaker:
    count = 0
    molarity2 = 0.0
    molarity3 =  0.0
    product = ''
    check = ''
    d = {1:['NaOH','H2SO4'], 2:['Na2SO4','H2O'],    #write a method to add stuff to array
     3:['HCl','NaOH'], 4:['NaCl','H2O'], 
     5:['Ba(OH)2','HNO3'], 6:['Ba(NO3)2','H2O']}
          
    d_balanced = {1:['2 NaOH','H2SO4'], 2:['Na2SO4','2 H2O'], 
     3:['HCl','NaOH'], 4:['NaCl','H2O'], 
     5:['Ba(OH)2','2 HNO3'], 6:['Ba(NO3)2','2 H2O']}
    
    array = []    
    
    def __init__(self, substance = None, amount = None, molarity= None):
                
        self.__substance = substance
        self.__amount = amount
        self.__molarity = molarity
        
        if substance == None:
            self.count = 0
        else:
            self.count = 1
                                    
    def add(self, substance, amount, molarity):
        
        if self.count == 0:
            self.__substance = substance
            self.__amount = amount
            self.__molarity = molarity
            self.array = [substance]
            self.count = 1
            
        elif self.count >= 1:
            self.count = 2
            self.__substance1 = substance
            self.__amount1 = amount
            self.__molarity1 = molarity
            self.array.append(substance)
            
    def inside(self):
     
        print 'Substance ', ' Volume (mL) ', ' Molarity (M)'
        print "  ", self.__substance, "      ", self.__amount, "        ", self.__molarity
            
        if self.count >= 2:
            print "  ", self.__substance1, "      ", self.__amount1, "        ", self.__molarity1
                    
            x = True  
            counter = 0
            
            while x is True:
                counter=counter+1
            
                if self.array == self.d[counter]:
                    print "  ",self.d[counter+1][0] , "    unknown         unknown"
                    print "  ",self.d[counter+1][1] , "     unknown         unknown"
                    x = False     
                
                       
            check = raw_input('Is all the data correct?  yes/no  :   ').lower()
             
            if check == 'yes':
                check = 'proceed'        

            else:
                print 'What would you like to ammend?'
                print '1 - Substance 1' 
                print '2 - Substance 2'
                print '3 - Both'
                
                option = input('Please enter the corresponding number:  ')
            
                while option < 10:
                    if option == 1:
                        option = 11
                        print 'Previous', self.__substance
                        self.__substance = raw_input('Enter new value:  ')
                        print 'Previous', self.__amount
                        self.__amount = input('Enter new value:  ')
                        print 'Previous', self.__molarity 
                        self.__molarity = input('Enter new value:  ')
                        
                    elif option == 2:
                        option = 11
                        print 'Previous', self.__substance1
                        self.__substance1 = raw_input('Enter new value:  ')
                        print 'Previous', self.__amount1
                        self.__amount1 = input('Enter new value:  ')
                        print 'Previous', self.__molarity1 
                        self.__molarity1 = input('Enter new value:  ')
                
                    elif option == 3:
                        option = 11
                        print 'Previous', self.__substance
                        self.__substance = raw_input('Enter new value:  ')
                        print 'Previous', self.__amount
                        self.__amount = input('Enter new value:  ')
                        print 'Previous', self.__molarity 
                        self.__molarity = input('Enter new value:  ')
                        print 'Previous', self.__substance1
                        self.__substance1 = raw_input('Enter new value:  ')
                        print 'Previous', self.__amount1
                        self.__amount1 = input('Enter new value:  ')
                        print 'Previous', self.__molarity1 
                        self.__molarity1 = input('Enter new value:  ')

                    else:
                        print 'Not an option'
                        option = 11


    def stoicheometry(self):

        totVolume = (self.__amount+self.__amount1)/1000
        
        #limiting reactant -------------------------------------------------------------

        x = True 
        counter = 0
                    
        while x is True:
            counter=counter+1
                    
            if self.array == self.d[counter]:
                x = False
                
                if self.d_balanced[counter][0][0].isdigit():
                    s_coeff= int(self.d_balanced[counter][0][0])
                else:
                    s_coeff = 1     
                    
                if self.d_balanced[counter][1][0].isdigit():
                    s1_coeff= int(self.d_balanced[counter][1][0])
                else:
                    s1_coeff = 1
                    
        moles = (self.__amount*(self.__molarity/1000))
        moles1 = (self.__amount1*(self.__molarity1/1000))
        
        testing = moles/s_coeff
        testing1 = moles1/s1_coeff
        
        if testing > testing1:
            limitReactNum = moles1
            s_coeff = s1_coeff
            
        elif testing1 > testing:
            limitReactNum = moles
            s1_coeff = s_coeff
            
        else:
            limitReactNum = moles
        
        #finding moles of products------------------------------------------------------
        
        if self.d_balanced[counter+1][0][0].isdigit():
            s_product_coeff= int(self.d_balanced[counter+1][0][0])
        else:
            s_product_coeff = 1     
                    
        if self.d_balanced[counter+1][1][0].isdigit():
            s1_product_coeff= int(self.d_balanced[counter+1][1][0])
        else:
            s1_product_coeff = 1
        
        molesOfProd = ((s_product_coeff)/(s_coeff))*limitReactNum
        molesOfProd1 = ((s1_product_coeff)/(s_coeff))*limitReactNum
        
        #Results------------------------------------------------------------------------
        
        self.molarity2 = molesOfProd/totVolume
        self.molarity3 =  molesOfProd1/totVolume
        
        print self.molarity2
        print self.molarity3              
    
    def outcome(self):
              
        x = True  
        counter = 0 
        
        while x is True:
            counter=counter+1
            
            if self.array == self.d[counter]:
                product = self.d_balanced[counter], '--->' ,self.d_balanced[counter+1]
                x = False
                self.count = 3
                
            else:
                product = 'no reaction'
    
        print product
        print 
        
        print 'Substance ', ' Volume (mL) ', ' Molarity (M)'
        print "  ", self.__substance, "      ", self.__amount, "        ", self.__molarity
            
        if self.count >= 2:
            print "  ", self.__substance1, "      ", self.__amount1, "        ", self.__molarity1
                    
            x = True  
            counter = 0
            totVolume = self.__amount +self.__amount1
            
            while x is True:
                counter=counter+1
            
                if self.array == self.d[counter]:
                    print "  ",self.d[counter+1][0] , "      ", totVolume, "        ", self.molarity2
                    print "  ",self.d[counter+1][1] , "      ", totVolume, "        ", self.molarity3
                    x = False                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    def rinse(self):
        
        if self.count >= 1:
            self.__substance = None
            self.__amount = None
            self.__molarity = None
            self.count = 0
            
        if self.count >= 2:
            self.__substance1 = None
            self.__amount1 = None
            self.__molarity1 = None
            self.count -= 1
