class Train:
    def __init__(self,category,first_station,last_station,position,speed):
        self.category = category
        self.first_station = first_station
        self.last_station = last_station
        self.position = position
        self.speed = speed

    def advance(self):
        self.position += self.speed

    def delay(self, minutes):
        self.position += minutes

    def accelerate(self, kmh):
        self.accelerate += kmh

    def decelerate(self, kmh):
        self.decelerate -= kmh