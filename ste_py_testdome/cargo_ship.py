'''
Created on 24.11.2020

@author: sbiker99-prog
'''

class CargoShip:
    
    def __init__(self, capacity):
        self.cargo = [("Lugano", 7), ("Cadro", 5)]
        self.capacity = capacity
        
    def unload(self, port):
        """
        :param port: (String)
        :returns: [(String, Int)]
        """
        result = []
        for mport, mweight in self.cargo:
            if mport == port:
                result.append((mport, mweight))
                self.cargo.remove((mport, mweight))
                
        return result
    
    def can_depart(self):
        """
        :returns: (Bool)
        """
        total = 0
        for mport, mweight in self.cargo:
            total += mweight
        
        return total <= self.capacity
    
    def load(self, new_cargo):
        """
        :param new_cargo: [(String, Int)]
        """
        self.cargo = self.cargo + new_cargo
    
if __name__ == "__main__":
    ship = CargoShip(10)
    print(ship.cargo)
    ship.load([("New York", 1), ("London", 20)])
    print(ship.cargo)
    print(ship.unload("Lugano"))
    print(ship.cargo)
    print(ship.can_depart()) #should print False