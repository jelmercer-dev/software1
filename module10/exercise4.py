import random

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


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        print(f"Race: {self.name}")
        print(f"{'License plate':<15}{'Maximum speed':<15}{'Current speed':<15}{'Distance':<15}")
        for car in self.cars:
            print(
                f"{car.license_plate:<15}"
                f"{car.maximum_speed:<15}"
                f"{car.current_speed:<15}"
                f"{car.travelled_distance:<15}"
            )

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)




