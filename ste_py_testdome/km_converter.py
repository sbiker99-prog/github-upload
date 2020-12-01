'''
Created on 24.11.2020

@author: sbiker99-prog
'''

class MilesToKmConverter:
    def get_miles_to_km_factor(self):
        return 1.609

    def miles_to_km(self, miles):
        return self.get_miles_to_km_factor() * miles

class NauticalMilesToKmConverter(MilesToKmConverter):
    def get_miles_to_km_factor(self):
        return 1.852
    
    def printFactors(self):
        print(self.get_miles_to_km_factor(), super().get_miles_to_km_factor())    
        
    def printFactors_self(self):
        print(self.get_miles_to_km_factor())    
        
    def printFactors_super(self):
        print(super().get_miles_to_km_factor())    
        
