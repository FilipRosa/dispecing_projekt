class Dispatcher:
    def __init__(self):
        self.trains = []

    def add_train(self, train):
        self.trains.append(train)

    def remove_train(self, train):
        self.trains.remove(train)

    def dellay_all_trains(self, minutes):
        for train in self.trains:
            train.delay(minutes)

    def accelerate_all_trains(self, kmh):
        for train in self.trains:
            train.accelerate(kmh)

    def decelerate_all_trains(self, kmh):
        for train in self.trains:
            train.decelerate(kmh)