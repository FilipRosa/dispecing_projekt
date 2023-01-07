import random
import functions

class Train:
    def __init__(self,id,category,number,first_station,last_station,delay,speed):
        self.id = id
        self.category = category
        self.number = number
        self.first_station = first_station
        self.last_station = last_station
        self.delay = delay
        self.speed = speed

#Úvodné texty
user_name = input("Zadaj svoje meno: ")

score = 0
level = 1

#Podmienka pre pokračovanie s užívateľským menom
while True:
    if user_name != "":

        print("Ahoj " + user_name + ", vitaj na pracovisku vlakového dispečingu pre trať Prievidza - Kraľovany!")

        #Dáta
        i = 0
        j = 0
        train_categories = ["Os","Zr","R"]
        train_stations = ["Prievidza","Žilina","Čadca","Kraľovany","Tekovany","..."]
        train_delays = [0, 5, 10]
        trains = []

        while score >= 0:
            #Výpis základných info /level, skóre/    
            print("")
            print("LEVEL ", level)
            print("")
            print("Tvoje skóre: ", score)
            print("")
            #Výpis vlakov + tabuľka
            print("Zoznam vlakov čakajúcich na spracovanie:")
            print("Id:     Kategória:     Číslo:     Počiatočná stanica:     Konečná stanica:     Meškanie:     Max.rýchlosť:")

            while i < level:
                #Získanie premenných z vlastných funkcií
                train_id = i
                train_category = functions.GetTrainCategory(train_categories)
                train_number = functions.GetTrainNumber(train_categories)
                train_first_station = functions.GetTrainFirstStation(train_stations)
                train_second_station = functions.GetTrainSecondStation(train_stations)
                train_delay = functions.GetTrainDelay(train_delays)
                train_speed = functions.GetTrainSpeed(train_categories)

                train = Train(train_id,train_category,train_number,train_first_station,train_second_station,train_delay,train_speed)
                
                trains.append(train)

                print(f"{str(train_id):<10}{str(train_category):<14}{str(train_number):<14}{str(train_first_station):<23}{str(train_second_station):<22}{str(train_delay):<16}{str(train_speed)}")

                i += 1

            #Úvodné texty 2
            print("")
            train_id = int(input("Vyber si vlak, ktorý chceš odbaviť tým, že napíšeš jeho id: "))

            selected_train = trains[train_id]

            train_category = selected_train.category
            train_number = selected_train.number
            train_first_station = selected_train.first_station
            train_second_station = selected_train.last_station

            train_station = functions.GetStations(train_category,train_first_station,train_second_station)
            print("Stanice vlaku ", train_number, " sú: ", train_station)
            print("")
            print("Teraz treba vybrať koľaje v jednotlivých staniciach, kde vlak zastavuje.")

            if level == 1 and (train_first_station == ['Tekovany'] or train_second_station == ['Tekovany']):
                print("POZOR!!! V žst. Žilina musí ísť vlak na koľaj 6, 7 alebo 8!")

            print("")

            for item in train_station:
                if item == "Prievidza" or item == "Nováky" or item == "Žilina" or item == "Čadca" or item == "Kraľovany":
                    print("Koľaj v stanici ", item," : ", end='')
                    track_number = input()

                    print(functions.IsTrackFree(item,track_number))

            

            trains.pop(train_id)

            print(trains)

            score -= 1

        print(user_name, " prehral si!")
        break
    else:
        user_name = input("Zadaj svoje meno!: ")