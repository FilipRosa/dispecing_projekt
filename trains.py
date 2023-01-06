class Train:
    def __init__(self,name,route,position,speed):
        self.name = name
        self.route = route
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