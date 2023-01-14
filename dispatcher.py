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

my_list = [{'train_id': 0, 'train_category': 'Os', 'train_number': 5009, 'train_first_station': 'Žilina', 'train_second_station': 'Tekovany', 'train_delay': 0, 'train_speed': 40}, {'train_id': 1, 'train_category': 'R', 'train_number': 718, 'train_first_station': 'Kraľovany', 'train_second_station': 'Tekovany', 'train_delay': 10, 'train_speed': 99}]

first_variable = my_list[0]
print(first_variable)