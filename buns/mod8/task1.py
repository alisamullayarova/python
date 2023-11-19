class Transport:
    def __init__(self, coordinates, speed, brand, year, number):
        self.coordinates = coordinates
        self.speed = speed
        self.brand = brand
        self.year = year
        self.number = number
        
    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, value):
        if isinstance(value, list):
            if (isinstance(value[0], int) and isinstance(value[1], int)
                    and isinstance(value[2], int) and isinstance(value[3], int)):
                if (value[0] >= 0 and value[1] >= 0 and value[2] >= 0 and value[3] >= 0):
                    self._coordinates = value
                else:
                    raise ValueError

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        if (isinstance(speed, int)
                and speed >= 0):
            self._speed = speed
        else:
            raise ValueError
        
    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        if isinstance(brand, str):
            self._brand = brand
        else:
            raise ValueError

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if (isinstance(year, int) and year > 0):
            self._year = year
        else:
            raise ValueError

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        if (isinstance(number, int) and (number > 0 and number <= 999999)):
            self._number = number
        else:
            raise ValueError
        
    def __str__(self):
        return f'Coordinates: {self.coordinates}, Speed: {self.speed}, Brand: {self.brand}, Year: {self.year}, Number: {self.number}'
        
    def isInArea(self, pos_x, pos_y, length, width):
        if (self.coordinates[0] >= pos_x and self.coordinates[0] <= pos_x + length and 
            self.coordinates[1] >= pos_y and self.coordinates[1] <= pos_y + width):
            return True
        else:
            return False

class Passenger:
    def __init__(self, passengers_capacity, number_of_passengers):
        self.passengers_capacity = passengers_capacity
        self.number_of_passengers = number_of_passengers

    @property
    def passengers_capacity(self):
        return self.__passengers_capacity
        
    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        if (isinstance(passengers_capacity, int) and passengers_capacity > 0):
            self._passengers_capacity = passengers_capacity
        else:
            raise ValueError
        
    @property
    def number_of_passengers(self):
        return self.__number_of_passengers
        
    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        if isinstance(number_of_passengers, int) and number_of_passengers >= 0:
            self._number_of_passengers = number_of_passengers
        else:
            raise ValueError
        
    def __str__(self):
        return f'Passengers_capacity: {self.passengers_capacity}, Number_of_passengers: {self.number_of_passengers}'

class Cargo:
    def __init__(self, carrying):
        self.carrying = carrying

    @property
    def carrying(self):
        return self.__carrying
        
    @carrying.setter
    def carrying(self, carrying):
        if isinstance(carrying, int) and carrying > 0:
            self._carrying = carrying
        else:
            raise ValueError

class Plane(Transport):
    def __init__(self, coordinates, speed, brand, year, number, height):
        super().__init__(coordinates, speed, brand, year, number)
        self.height = height

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if isinstance(height, int) and height >= 0:
            self._height = height
        else:
            raise ValueError
        
class Auto(Transport):
    def __init__(self, coordinates, speed, brand, year, number, license):
        super().__init__(coordinates, speed, brand, year, number)
        self.license = license

    @property
    def license(self):
        return self._license

    @license.setter
    def license(self, license):
        if isinstance(license, str) and len(license) == 6:
            self._license = license
        else:
            raise ValueError
        
class Ship(Transport):
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number)
        self.port = port

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        if isinstance(port, str):
            self._port = port
        else:
            raise ValueError

class Car(Auto):
    def __init__(self, coordinates, speed, brand, year, number, license):
        super.__init__(self, coordinates, speed, brand, year, number, license)

class Bus(Auto, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, license, passengers_capacity, number_of_passengers):
        Auto.__init__(self, coordinates, speed, brand, year, number, license)
        Passenger.__init__(self, passengers_capacity, number_of_passengers)

class CargoAuto(Auto, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, license, carrying):
        Auto.__init__(self, coordinates, speed, brand, year, number, license)
        Cargo.__init__(self, carrying)

class Boat(Ship):
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(coordinates, speed, brand, year, number, port)

class PassengerShip(Ship, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, port, passengers_capacity, number_of_passengers):
        Ship.__init__(coordinates, speed, brand, year, number, port)
        Passenger.__init__(self, passengers_capacity, number_of_passengers)

class CargoShip(Ship, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, port, carrying):
        Ship.__init__(coordinates, speed, brand, year, number, port)
        Cargo.__init__(self, carrying)

class SeaPlane(Plane, Ship):
    def __init__(self, coordinates, speed, brand, year, number, height, port, model):
        Transport.__init__(self, coordinates, speed, brand, year, number)
        Ship._port = port
        Plane._height = height
        self.model = model

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        if isinstance(model, str):
            self._model = model
        else:
            raise ValueError 
        
class PassengerPlane(Plane, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, height, passengers_capacity, number_of_passengers):
        Plane.__init__(self, coordinates, speed, brand, year, number, height)
        Passenger.__init__(self, passengers_capacity, number_of_passengers)
        
class CargoPlane(Plane, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, height, passengers_capacity, carrying):
        Plane.__init__(self, coordinates, speed, brand, year, number, height)
        Cargo.__init__(self, carrying)

seaplane = SeaPlane([1, 2, 3, 4], 250, 'booing', 1997, 753704, 3200, '235-us', 'aa297g')
print(seaplane.model)
