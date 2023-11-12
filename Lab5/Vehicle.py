class Vehicle:
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year

    def __str__(self):
        info = str(self._make) + " " + str(self._model) + " " + str(self._year)
        return info


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors, fuel_efficiency):
        super().__init__(make, model, year)
        self._num_doors = num_doors
        self._fuel_efficiency = fuel_efficiency

    def calculate_mileage(self, driven_distance):
        return driven_distance / self._fuel_efficiency

    def get_number_doors(self):
        x = self._num_doors
        return x

    def get_fuel_efficiency(self):
        x = self._fuel_efficiency
        return x


class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity, curb_weight):
        super().__init__(make, model, year)
        self._towing_capacity = towing_capacity
        self._curb_weight = curb_weight

    def calculate_towing_capacity(self):
        capacity = self._towing_capacity - self._curb_weight
        return max(capacity, 0)

    def get_towing_capacity(self):
        x = self._towing_capacity
        return x

    def get_curb_weight(self):
        x = self._curb_weight
        return x


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, num_wheels, fuel_efficiency):
        super().__init__(make, model, year)
        self._num_wheels = num_wheels
        self._fuel_efficiency = fuel_efficiency

    def calculate_mileage(self, driven_distance):
        return driven_distance / self._fuel_efficiency

    def get_fuel_efficiency(self):
        x = self._fuel_efficiency
        return x

    def get_number_wheels(self):
        x = self._num_wheels
        return x


car = Car("Mercedes", "GLS", 2023, 4, 50)

print("Car Info:", str(car))
print("Number of Doors:", car.get_number_doors())
print("Fuel Efficiency:", car.get_fuel_efficiency())
print("Mileage for 100 km:", car.calculate_mileage(100))

truck = Truck("Trunk", "zyx", 2012, 10000, 5000)

print("Truck Info:", str(truck))
print("Towing Capacity:", truck.get_towing_capacity())
print("Curb Weight:", truck.get_curb_weight())
print("Effective Towing Capacity:", truck.calculate_towing_capacity())

motorcycle = Motorcycle("moto", " x ", 2020, 2, 30)

print("Motorcycle Info:", str(motorcycle))
print("Number of Wheels:", motorcycle.get_number_wheels())
print("Fuel Efficiency:", motorcycle.get_fuel_efficiency())
print("Mileage for 100 km:", motorcycle.calculate_mileage(100))
