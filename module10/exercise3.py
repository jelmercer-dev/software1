class Elevator:

    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor
        

    def go_to_floor(self, floor):
        while self.current_floor < floor:
            self.floor_up()
        while self.current_floor > floor:
            self.floor_down()

    def floor_up(self):
            self.current_floor += 1
            print(f"The elevator is now on floor {self.current_floor}")


    def floor_down(self):
            self.current_floor -= 1
            print(f"The elevator is now on floor {self.current_floor}")



class Building:
    def __init__(self, bottom_floor, top_floor, elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [ Elevator(bottom_floor, top_floor) for _ in range(elevators) ]

    def run_elevator(self, elevators, floor):
        self.elevators[elevators].go_to_floor(floor)

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)
