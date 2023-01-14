import random
import functions
import re
import time

class Train:
    def __init__(self):
        self.train_field = []

    #funkcia pre pridanie do poľa
    def ToField(self, train_id, train_category, train_number, train_first_station, train_second_station, train_delay, train_speed):
        variable = {'train_id': train_id, 'train_category': train_category, 'train_number' : train_number, 'train_first_station' : train_first_station, 'train_second_station': train_second_station, 'train_delay': train_delay, 'train_speed': train_speed}
        self.train_field.append(variable)

    #funkcia pre odstránenie z poľa
    def DelField(self, id):
        self.train_field = [var for var in self.train_field if var['train_id'] != id]

    #funkcia pre vypísanie z poľa
    def PrintField(self):
        for item in self.train_field:
            print(f"{str(item['train_id']):<10}{str(item['train_category']):<14}{str(item['train_number']):<14}{str(item['train_first_station']):<23}{str(item['train_second_station']):<22}{str(item['train_delay']):<16}{str(item['train_speed'])}")


    #funkcia pre určenie medziľahlých staníc vlaku
    def GetStations(self):
        #osobný vlak
        if self.category == ['Os']:
            if self.first_station == ['Prievidza']:
                if self.last_station == ['Čadca']:
                    return ['Koš','Nováky','Partizánske','Žilina-východ','Žilina','Lučivná']
                elif self.last_station == ['Žilina']:
                    return ['Koš','Nováky','Partizánske','Žilina-východ']
                elif self.last_station == ['Kraľovany']:
                    return ['Koš','Nováky','Partizánske','Žilina-východ','Žilina','Lučivná','Čadca']
                elif self.last_station == ['...']:
                    return ['Koš','Nováky','Partizánske','Žilina-východ','Žilina','Lučivná','Čadca','Kraľovany']
                elif self.last_station == ['Tekovany']:
                    return ['Koš','Nováky','Partizánske','Žilina-východ','Žilina','Žilina-Hájik']
            elif self.first_station == ['Žilina']:
                if self.last_station == ['Čadca']:
                    return ['Lučivná']
                elif self.last_station == ['Prievidza']:
                    return ['Žilina-východ','Partizánske','Nováky','Koš']
                elif self.last_station == ['Kraľovany']:
                    return ['Lučivná','Čadca']
                elif self.last_station == ['...']:
                    return ['Lučivná','Čadca','Kraľovany']
                elif self.last_station == ['Tekovany']:
                    return ['Žilina-Hájik']
            elif self.first_station == ['Čadca']:
                if self.last_station == ['Žilina']:
                    return ['Lučivná']
                elif self.last_station == ['Prievidza']:
                    return ['Lučivná','Žilina','Žilina-východ','Partizánske','Nováky','Koš']
                elif self.last_station == ['Kraľovany']:
                    return ['']
                elif self.last_station == ['...']:
                    return ['Kraľovany']
                elif self.last_station == ['Tekovany']:
                    return ['Lučivná','Žilina','Žilina-Hájik']
            elif self.first_station == ['Kraľovany']:
                if self.last_station == ['Žilina']:
                    return ['Čadca','Lučivná']
                elif self.last_station == ['Prievidza']:
                    return ['Čadca','Lučivná','Žilina','Žilina-východ','Partizánske','Nováky','Koš']
                elif self.last_station == ['Čadca']:
                    return ['']
                elif self.last_station == ['...']:
                    return ['']
                elif self.last_station == ['Tekovany']:
                    return ['Čadca','Lučivná','Žilina','Žilina-Hájik']
            elif self.first_station == ['...']:
                if self.last_station == ['Žilina']:
                    return ['Kraľovany','Čadca','Lučivná']
                elif self.last_station == ['Prievidza']:
                    return ['Kraľovany','Čadca','Lučivná','Žilina','Žilina-východ','Partizánske','Nováky','Koš']
                elif self.last_station == ['Čadca']:
                    return ['Kraľovany']
                elif self.last_station == ['Kraľovany']:
                    return ['']
                elif self.last_station == ['Tekovany']:
                    return ['Kraľovany','Čadca','Lučivná','Žilina','Žilina-Hájik']
            elif self.first_station == ['Tekovany']:
                if self.last_station == ['Žilina']:
                    return ['Žilina-Hájik']
                elif self.last_station == ['Prievidza']:
                    return ['Žilina-Hájik','Žilina','Žilina-východ','Partizánske','Nováky','Koš']
                elif self.last_station == ['Čadca']:
                    return ['Žilina-Hájik','Žilina','Lučivná']
                elif self.last_station == ['Kraľovany']:
                    return ['Žilina-Hájik','Žilina','Lučivná','Čadca']
                elif self.last_station == ['...']:
                    return ['Žilina-Hájik','Žilina','Lučivná','Čadca','Kraľovany']   
        #zrýchlený vlak    
        elif self.category == ['Zr']:
            if self.first_station == ['Prievidza']:
                if self.last_station == ['Čadca']:
                    return ['Nováky','Partizánske','Žilina-východ','Žilina']
                elif self.last_station == ['Žilina']:
                    return ['Nováky','Partizánske','Žilina-východ']
                elif self.last_station == ['Kraľovany']:
                    return ['Nováky','Partizánske','Žilina-východ','Žilina','Čadca']
                elif self.last_station == ['...']:
                    return ['Nováky','Partizánske','Žilina-východ','Žilina','Čadca','Kraľovany']
                elif self.last_station == ['Tekovany']:
                    return ['Nováky','Partizánske','Žilina-východ','Žilina']
            elif self.first_station == ['Žilina']:
                if self.last_station == ['Čadca']:
                    return ['']
                elif self.last_station == ['Prievidza']:
                    return ['Žilina-východ','Partizánske','Nováky']
                elif self.last_station == ['Kraľovany']:
                    return ['Čadca']
                elif self.last_station == ['...']:
                    return ['Čadca','Kraľovany']
                elif self.last_station == ['Tekovany']:
                    return ['']
            elif self.first_station == ['Čadca']:
                if self.last_station == ['Žilina']:
                    return ['']
                elif self.last_station == ['Prievidza']:
                    return ['Žilina','Žilina-východ','Partizánske','Nováky']
                elif self.last_station == ['Kraľovany']:
                    return ['']
                elif self.last_station == ['...']:
                    return ['Kraľovany']
                elif self.last_station == ['Tekovany']:
                    return ['Žilina']
            elif self.first_station == ['Kraľovany']:
                if self.last_station == ['Žilina']:
                    return ['Čadca']
                elif self.last_station == ['Prievidza']:
                    return ['Čadca','Žilina','Žilina-východ','Partizánske','Nováky']
                elif self.last_station == ['Čadca']:
                    return ['']
                elif self.last_station == ['...']:
                    return ['']
                elif self.last_station == ['Tekovany']:
                    return ['Čadca','Žilina']
            elif self.first_station == ['...']:
                if self.last_station == ['Žilina']:
                    return ['Kraľovany','Čadca']
                elif self.last_station == ['Prievidza']:
                    return ['Kraľovany','Čadca','Žilina','Žilina-východ','Partizánske','Nováky']
                elif self.last_station == ['Čadca']:
                    return ['Kraľovany']
                elif self.last_station == ['Kraľovany']:
                    return ['']
                elif self.last_station == ['Tekovany']:
                    return ['Kraľovany','Čadca','Žilina']
            elif self.first_station == ['Tekovany']:
                if self.last_station == ['Žilina']:
                    return ['']
                elif self.last_station == ['Prievidza']:
                    return ['Žilina','Žilina-východ','Partizánske','Nováky']
                elif self.last_station == ['Čadca']:
                    return ['Žilina']
                elif self.last_station == ['Kraľovany']:
                    return ['Žilina','Čadca']
                elif self.last_station == ['...']:
                    return ['Žilina','Čadca','Kraľovany']
        #rýchlik   
        elif self.category == ['R']:
            if self.first_station == ['Prievidza']:
                if self.last_station == ['Čadca']:
                    return ['Partizánske','Žilina']
                elif self.last_station == ['Žilina']:
                    return ['Partizánske']
                elif self.last_station == ['Kraľovany']:
                    return ['Partizánske','Žilina','Čadca']
                elif self.last_station == ['...']:
                    return ['Partizánske','Žilina','Čadca','Kraľovany']
                elif self.last_station == ['Tekovany']:
                    return ['Partizánske','Žilina']
            elif self.first_station == ['Žilina']:
                if self.last_station == ['Čadca']:
                    return ['']
                elif self.last_station == ['Prievidza']:
                    return ['Partizánske']
                elif self.last_station == ['Kraľovany']:
                    return ['Čadca']
                elif self.last_station == ['...']:
                    return ['Čadca','Kraľovany']
                elif self.last_station == ['Tekovany']:
                    return ['']
            elif self.first_station == ['Čadca']:
                if self.last_station == ['Žilina']:
                    return ['']
                elif self.last_station == ['Prievidza']:
                    return ['Žilina','Partizánske']
                elif self.last_station == ['Kraľovany']:
                    return ['']
                elif self.last_station == ['...']:
                    return ['Kraľovany']
                elif self.last_station == ['Tekovany']:
                    return ['Žilina']
            elif self.first_station == ['Kraľovany']:
                if self.last_station == ['Žilina']:
                    return ['Čadca']
                elif self.last_station == ['Prievidza']:
                    return ['Čadca','Žilina','Partizánske']
                elif self.last_station == ['Čadca']:
                    return ['']
                elif self.last_station == ['...']:
                    return ['']
                elif self.last_station == ['Tekovany']:
                    return ['Čadca','Žilina']
            elif self.first_station == ['...']:
                if self.last_station == ['Žilina']:
                    return ['Kraľovany','Čadca']
                elif self.last_station == ['Prievidza']:
                    return ['Kraľovany','Čadca','Žilina','Partizánske']
                elif self.last_station == ['Čadca']:
                    return ['Kraľovany']
                elif self.last_station == ['Kraľovany']:
                    return ['']
                elif self.last_station == ['Tekovany']:
                    return ['Kraľovany','Čadca','Žilina']
            elif self.first_station == ['Tekovany']:
                if self.last_station == ['Žilina']:
                    return ['']
                elif self.last_station == ['Prievidza']:
                    return ['Žilina','Partizánske']
                elif self.last_station == ['Čadca']:
                    return ['Žilina']
                elif self.last_station == ['Kraľovany']:
                    return ['Žilina','Čadca']
                elif self.last_station == ['...']:
                    return ['Žilina','Čadca','Kraľovany']






class Track:
    def __init__(self,station,track):
        self.station = station
        self.track = track

    #funkcia na zistenie voľnosti koľaje
    def IsFree(self,stations): 
        if stations[self.station][self.track] == True:
            stations[self.station][self.track] = False
            print("Žiadosť o obsadenie koľaje úspešná.")
        elif stations[self.station][self.track] == False:
            print("Koľaj obsadená.")

    #funkcia na vypísanie obsadenosti koľají
    def StillFree(self,stations):
        i = 1

        if self.station == "...":
            pass
        else:
            for item in stations[self.station]:
                if item == True:
                    print("Koľaj č. ", i, " v stanici ", functions.GetNameOfStation(self.station), " je voľná.")
                    i += 1
                elif item == False:
                    print("Koľaj č. ", i, " v stanici ", functions.GetNameOfStation(self.station), " je obsadená.")
                    i += 1

            print("")

    #funkcia na sekvenciu
    def Sequence(self,train_category,train_number,stations):
        print(train_category, train_number, " prichádza do stanice ", functions.GetNameOfStation(self.station))
        time.sleep(2)
        print(train_category, train_number, " odišiel zo stanice ", functions.GetNameOfStation(self.station))

        if stations[self.station][self.track] == False:
            stations[self.station][self.track] = True

        
        time.sleep(2)


#Úvodné texty
user_name = input("Zadaj svoje meno: ")

#Dáta
score = 0
level = 1

j = 0
train_id = 0
train_categories = ["Os","Zr","R"]
train_stations = ["Prievidza","Žilina","Čadca","Kraľovany","Tekovany","..."]
train_delays = [0, 5, 10]
trains = []

stations = [
    [True,True,True,True,True,True], #prievidza
    [True], #koš
    [True,True,True], #nováky
    [True], #partizánske
    [True], #žilina východ
    [True,True,True,True,True,True,True,True], #žilina
    [True], #žilina hájik
    [True], #tekovany
    [True], #lučivná
    [True,True,True,True], #čadca
    [True,True], #kraľovany
    [True] #...
]

game = True

#Podmienka pre pokračovanie s užívateľským menom
while game == True:
    if user_name != "":

        print("Ahoj " + user_name + ", vitaj v hre VLAKOVÝ DISPEČING!")
        print("...pokyny...")

        while score >= 0:
            #Výpis základných info /level, skóre/    
            print("")
            print("---------------------------------------")
            print("LEVEL ", level)
            print("")
            print("Tvoje skóre: ", score)
            print("")

            i = 0
            
            print("Id:     Kategória:     Číslo:     Počiatočná stanica:     Konečná stanica:     Meškanie:     Max.rýchlosť:")

            


            while i < level:
                #Získanie premenných z vlastných funkcií
                train_category = functions.GetTrainCategory(train_categories)
                train_number = functions.GetTrainNumber(train_category)
                train_first_station = functions.GetTrainFirstStation(train_stations)
                train_second_station = functions.GetTrainSecondStation(train_stations,train_first_station)
                train_delay = functions.GetTrainDelay(train_delays)
                train_speed = functions.GetTrainSpeed(train_category)

                #Ošetrenie generovania rovnakých staníc
                while train_first_station == train_second_station:
                    train_first_station = functions.GetTrainFirstStation(train_stations)
                    train_second_station = functions.GetTrainSecondStation(train_stations,train_first_station)

                #Vyhodenie prvkov z poľa
                for item in train_category:
                    train_category = item

                for item in train_first_station:
                    train_first_station = item

                for item in train_second_station:
                    train_second_station = item

                for item in train_delay:
                    train_delay = item

                train = Train()
                train.ToField(train_id,train_category,train_number,train_first_station,train_second_station,train_delay,train_speed)
                train.PrintField()
                

                
                
                train_id += 1
                
                i += 1
                

            while len(trains) >= 1:
                #Výpis vlakov + tabuľka
                print("Zoznam vlakov čakajúcich na spracovanie:")
                
                
                

                #Úvodné texty 2
                print("")
                train_id = int(input("Vyber si vlak, ktorý chceš odbaviť tým, že napíšeš jeho id: "))

                #Ošetrenie nesprávne zadaného id-čka
                trains_lenght = len(trains)

                while trains_lenght < (train_id + 1):
                    print("Nevybral si správne vlak.")
                    train_id = int(input("Vyber si vlak, ktorý chceš odbaviť tým, že napíšeš jeho id: "))
                    
                selected_train = trains[train_id]

                train_category = selected_train.category
                train_number = selected_train.number
                train_first_station = selected_train.first_station
                train_second_station = selected_train.last_station

                train_station = Train(train_id,train_category,train_number,train_first_station,train_second_station,train_delay,train_speed).GetStations()

                #Poriešenie riešenia bez medziľahlých staníc
                if train_station == ['']:
                    print("Vlak ", train_category, train_number, " nemá žiadne medziľahlé stanice.")

                    print("Teraz treba vybrať koľaje v jednotlivých staniciach, kde vlak zastavuje.")

                    #Výpis voľnosti koľají
                    for item in train_second_station:
                        track_auto_number = 0
                        item = functions.GetItem(item)
                        Track(item,track_auto_number).StillFree(stations)
                        track_auto_number += 1

                else:
                    print("Medziľahlé stanice vlaku ", train_category, train_number, " sú: ", train_station)
                    print("")
                    time.sleep(2)

                    print("Teraz treba vybrať koľaje v jednotlivých staniciach, kde vlak zastavuje.")

                    #Výpis voľnosti koľají
                    for item in train_station:
                        track_auto_number = 0
                        item = functions.GetItem(item)
                        Track(item,track_auto_number).StillFree(stations)
                        track_auto_number += 1

                    for item in train_second_station:
                        track_auto_number = 0
                        item = functions.GetItem(item)
                        Track(item,track_auto_number).StillFree(stations)
                        track_auto_number += 1


                if level <= 5 and (train_first_station == ['Tekovany'] or train_second_station == ['Tekovany']):
                    print("POZOR!!! V žst. Žilina musí ísť vlak na koľaj 6, 7 alebo 8!")

                print("")

                #Zadávanie koľají
                for item in train_station:
                    if item == "Prievidza" or item == "Nováky" or item == "Žilina" or item == "Čadca" or item == "Kraľovany":
                        print("Koľaj v stanici ", item," : ", end='')
                        track_number = int(input()) - 1

                        item = functions.GetItem(item)

                        Track(item,track_number).IsFree(stations)
                    elif item == "" or item == "...":
                        pass

                #Odstránenie zátvoriek z reťazca
                for x in train_second_station:
                    item = x
                    
                #Zadanie koľaje poslednej stanice
                if item == "Prievidza" or item == "Žilina" or item == "Čadca" or item == "Kraľovany":
                    print("Koľaj v konečnej stanici ", item," : ", end='')
                    track_number = int(input()) - 1

                    item = functions.GetItem(item)

                    Track(item,track_number).IsFree(stations)
                elif item == "...":
                    pass

                #Začiatok riešenia pohybu vlaku
                print("")

                print(train_category, train_number, " odchádza zo stanice ", train_first_station)

                if train_station == ['']:
                    print(train_category, train_number, " prichádza do stanice ", train_second_station)
                else:
                    for item in train_station:
                        item = functions.GetItem(item)
                        x = functions.GetNameOfStation(item)

                        if x != train_second_station and x != "...":
                            Track(item,track_number).Sequence(train_category,train_number,stations)
                            
                    print(train_category, train_number, " prichádza do stanice ", train_second_station)

                trains.pop(train_id)

                score += 10

            level += 1

            #GameOver
            if score < 0:
                print(user_name, " prehral si!")
                game = False
    else:
        user_name = input("Zadaj svoje meno!: ")



