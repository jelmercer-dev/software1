class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        if self.current_speed + change >= self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed + change <= 0:
            self.current_speed = 0
        else:
            self.current_speed += change

    def drive(self, number_of_hours):
        self.travelled_distance += number_of_hours * self.current_speed

class ElectricCar(Car):
    def __init__(self, license_plate, maximum_speed, battery_capacity):
        super().__init__(maximum_speed, license_plate)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, license_plate, maximum_speed, tank_volume):
        super().__init__(license_plate, maximum_speed)
        self.tank_volume = tank_volume