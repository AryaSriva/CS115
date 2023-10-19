'''
CS 115, Lab 12, Inheritance

Author: <your name here>
Pledge: <write pledge>
'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Part 1 
' Implement missing sections of the Car class.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Car(object):
    '''Write the constructor. It should take in four arguments:
       - make (a string, the company name, a.k.a. brand)
       - model (a string)
       - mpg (miles per gallon, a float)
       - tank_capacity (capacity of the gas tank in gallons, a float)
       These should all be assigned to corresponding private fields, i.e., with
       names that start with '__'.  Use the names in the 'str' method provided below.
       '''
        def __init__(self, make, model, mpg, tank_capacity):
            '''constructor: makes a car object with the attributes:
            make, name, mpg, tank capacity, all of which are private varibales'''
            self.__make = make
            self.__model = model
            self.__mpg = mpg
            self.__tank_capacity = tank_capacity

    '''Write getters for make, model, mpg, and tank_capacity.'''
        def getMake(self):
            '''returns make of car object'''
            return self.__make
        
        def getModel(self):
            '''returns model of car object'''
            return self.__model
        
        def getMPG(self):
            '''returns mpg of car object'''
            return self.__model
        
        def getTankCapacity(self):
            '''returns tank capacity of car object'''
            return self.__model
        
        def setMPG(self, mpg):
            '''sets mpg of car object to a given number'''
            self.__mpg = mpg

        def setTankCapacity(self, tank_capacity):
            '''sets tank capacity of car object to a given number'''
            self.__tank_capacity = tank_capacity

    '''Write setters for mpg and tank_capacity.'''

    '''Write a method called get_total_range.
       It returns the total distance the car can travel on a full tank of
       gas.'''
        def get_total_range(self):
            '''returns the total distance the car can travel on a full tank of gas'''
            return self.__mpg*self.__tank_capacity


    def __str__(self):
        '''A string for printing information about a car.'''
        return self.__make + ' ' + self.__model + ', MPG: ' + str(self.__mpg) \
            + ', tank capacity: ' + str(self.__tank_capacity)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Part 2 
' Implement missing sections of the HybridCar class. 
' Make HybridCar be a subclass of Car.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class HybridCar(Car):  
    '''Write the constructor. It should take in 6 arguments:
    - the first four are the same as in the Car constructor
    - battery_kWh (battery power in kilowatt-hours, a float)
    - miles_per_kWh (miles per kilowatt-hours, a float)
    The additional fields must be private.
    '''
    def __init__(self, make, model, mpg, tank_capacity, battery_kWh, miles_per_kWh):
        '''constructor: make a HybridCar object with the same attributes as a car object and
            a battery_kWh and miles_per_kWh attribute'''
        Car.__init__(make, model, mpg, tank_capacity)
        self.__battery_kWh = battery_kWh
        self.__miles_per_kWh = miles_per_kWh

    '''Implement the following method.'''
    def get_battery_range(self):
        '''Returns the total distance the car can travel on a fully charged
        battery.
        '''
        return self.battery_kWh*miles_per_kWh
 

    '''Override the method get_total_range.
    Returns the total distance the car can travel on a full tank of
    gas and a fully charged battery.
    Do not do any math here except a single +. To get credit, you must call
    the methods you have already written.
    '''
    def get_total_range(self):
        '''Returns the total distance the car can travel on a fully charged battery and a full tank of gas'''
        return self.get_total_range + self.get_battery_range

    def __str__(self):
        '''A string for printing information about a car.'''
        return super().__str__() + ', battery kWh: ' + \
            str(self.__battery_kWh) + ', miles/kWh: ' + \
            str(self.__miles_per_kWh)