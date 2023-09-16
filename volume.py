############################################################################################################################
#  Project 11
#
# Create a Class name Volume that will get the magnitude and the units in two system and calculate and convert from one systm to one another
#
# the first method an will instiliaze the constroucter and add a default value of magintude and the unit
#
# STR method will check if the unit is assigned to None or not, if not it will return the magnitude with the specified format
# 
# create RPR method, This method will check if the unit is valid or not and return the magnitude and the unit 
#
# create a valid method, This method will check if the magnitude is valid or not
#
# create a method that will calculate the difference between the two systems
#
############################################################################################################################


UNITS = ["ml","oz"]
MLperOZ = 29.5735295625  # ml per oz
DELTA = 0.000001

class Volume(object):
    def __init__(self,magnitude = 0 ,units = "ml"):   # This line will instiliaze the constroucter and add a default value of magintude and the unit
        '''This will instiliaze the constroucter and add a default value of magintude and the unit '''
        if magnitude >=0 and type(magnitude) == float or str(magnitude).isdigit(): # check if the magnitude is valid 
            if units == "ml" or units == "oz": # check if the unit is ml or oz
                self.magnitude= magnitude # assign the value to magnitude
                self.unit = units
            else:
                self.magnitude = None # assign a none value to magnitude
                self.unit = None # assign a none value to unit
        else:
            self.magnitude = 0 #assgin a value for magintude 
            self.unit = None

        

    def __str__(self):    
        '''This method will check if the unit is assigned to None or not, if not it will return the magnitude with the specified format '''
        if self.unit == None: #check if the unit
            return 'Not a Volume'
        else:
            return "{:.3f} {}".format(self.magnitude,self.unit) #return the maganutide and the unit with specified value 
        
        
    def __repr__(self):    
        '''This method will check if the unit is valid or not and return the magnitude and the unit '''
        if self.unit == None:
            return 'Not a Volume'
        else:
            return ("{:.6f} {}".format(self.magnitude,self.unit))
        
    def is_valid(self):     
        '''This method will check if the magnitude is valid or not''' 
        if (self.magnitude != 0 and self.unit != None) or (self.magnitude != None and self.unit != None): # check if the magnitude is valid or not
            return True
        else:
            return False
    
    def get_units(self):     
        ''' Returns units stored "ml" or "oz" if V is valid, None otherwise'''
        if (self.magnitude != 0 and self.unit != None) or (self.magnitude != None and self.unit != None): # check if the magnitude is  valid or not
            return self.unit # return the value if it was valid
        else:
            return None
        
    
    def get_magnitude(self):  
        '''This method will return the magnitude if it was valid '''
        if (self.magnitude != None):# check if the magnitude is valid or not and return the value of it if so
            return self.magnitude
        else:
            return None # return None Otherwise


        
    
    def metric(self):      
        '''This method will convert the unit from oz to ml '''
        if self.unit == "oz" :#check if the  unit is oz
            ml= MLperOZ * self.magnitude # multiply the value in the document with the magintude to conver it
            return Volume(ml,"ml")# return ml
        elif self.unit == "ml":# check if the unit is ml
            ml = self.magnitude
            return Volume(magnitude,"ml")
        elif self.unit == None:# return None if the unit is none
            return Volume(-4, None)

        
        
    def customary(self):    
        '''create a method that will check if the method is in us system'''
        if self.unit == "ml":
            oz= self.magnitude / MLperOZ  # covert it by deviding the magnitude over the given value
            return Volume(oz,"oz") # return the converted magnitude with a unit value
        elif self.unit == "oz":
            oz= self.magnitude
            return Volume(oz,"oz")# return the converted magnitude with a unit value
        elif self.unit == None: # return none if the value is none
            return Volume(-5,None)# return none none if it was invalid
        
        
    def __eq__(self, V2):  
        '''This method will check if it was the bigger value '''
        if DELTA > abs(self.magnitude - V2.magnitude): # check if the value of delta is bigger than the absolur value of the difference
            return True
        else:
            return False
       
    def add(self,v2):  
        '''This method will add two volumes and take into considreation '''
        if type(v2) == Volume:
            if self.unit != None: # check if the unit is None or not

                if self.unit == v2.unit:# check if the self unit is the same as v2 unit
                    return Volume((self.magnitude + v2.magnitude ),self.unit)# using the volume class add the magintude values 
                elif self.unit == "ml" and v2.unit == "oz": # check if the units were ml and oz
                    new_v2 = v2.metric()
                    if new_v2.is_valid() == True:# check if the code is  valid or not
                        return Volume(self.magnitude +new_v2.magnitude,"ml") # add the magnitudes and  return the volume class with it
                    else:
                        return Volume(-4, None)
                elif self.unit == "oz" and v2.unit == "ml": # check if the units were ml and oz
                    new_v2 = v2.customary()
                    if new_v2.is_valid() == True: # check if the code is  valid or not
                        return Volume(self.magnitude +new_v2.magnitude,"oz") # add the magnitudes and  return the volume class with it
                    else:
                        return Volume(-4, None) # return  none otherwise
                else:
                    return Volume(-4, None) # return  none otherwise
            else:
                return Volume(-4, None)# return  none otherwise
        else:
            return Volume(self.magnitude+v2,self.unit)

    
    def sub(self,v2): 
        '''This method will substract two volumes and take into considreation'''
        if type(v2) == Volume:
            if self.unit != None: # check if the unit is None or not

                if self.unit == v2.unit: # check if the self unit is the same as v2 unit
                    return Volume((self.magnitude - v2.magnitude ),self.unit) # using the volume class substract the magintude values 
                elif self.unit == "ml" and v2.unit == "oz":
                    new_v2 = v2.metric()
                    if new_v2.is_valid() == True:
                        return Volume(self.magnitude - new_v2.magnitude,"ml")# add the magnitudes and  return the volume class with it
                    else:
                        return Volume(-4, None)
                elif self.unit == "oz" and v2.unit == "ml": # check if the unit is None or not
                    new_v2 = v2.customary()
                    if new_v2.is_valid() == True:
                        return Volume(self.magnitude - new_v2.magnitude,"oz")# add the magnitudes and  return the volume class with it
                    else:
                        return Volume(-4, None) # return  none otherwise
            else:
                return Volume(-4, None) # return  none otherwise
        else:
            return Volume(self.magnitude-v2,self.unit)
