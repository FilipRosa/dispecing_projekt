import functions
import time
import os

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

        if self.station == "..." or self.station == "Koš" or self.station == "Partizánske" or self.station == "Žilina-východ" or self.station == "Žilina-Hájik" or self.station == "Lučivná":
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
train_categories = ['Os','Zr','R']
train_stations = ['Prievidza','Žilina','Čadca','Kraľovany','Tekovany','...']
train_delays = [0, 5, 10]
game = True


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

if game == True:
    #Podmienka pre pokračovanie s užívateľským menom
    if user_name != "":
        #Privítanie + pokyny
        print("Ahoj " + user_name + ", vitaj v hre VLAKOVÝ DISPEČING!")
        time.sleep(0.5)
        print("...pokyny...")
        time.sleep(2)

        #Podmienka pre ukončenie hry so skóre < 0
        if score >= 0:
            train_field = []
            while_counter = 1

            #Cyklus pre opakovanie
            while True:
                #Výpis levelu a skóre    
                print("")
                print("---------------------------------------")
                print("LEVEL ", level)
                print("")
                print("Tvoje skóre: ", score)
                print("")
                print("Id:     Kategória:     Číslo:     Počiatočná stanica:     Konečná stanica:     Meškanie:     Max.rýchlosť:")
                
                i = 0
                train_id = 0
                
                

                while i < level:
                    field_lenght = len(train_field)
                    false_lenght = field_lenght - 1
                    if not train_field or false_lenght < i:
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

                        #Vyhodenie stringov z poľa
                        for item in train_category:
                            train_category = item

                        for item in train_first_station:
                            train_first_station = item

                        for item in train_second_station:
                            train_second_station = item

                        for item in train_delay:
                            train_delay = item

                        check = open("check.txt", "a")
                        check.write(str(i))
                        check.close
                        check = open("check.txt","r")

                        if while_counter == level:
                            train_field.insert(i,functions.ToField(train_id,train_category,train_number,train_first_station,train_second_station,train_delay,train_speed))
                        else:
                            pass

                            #for x in check:
                             #   if x == str(i):
                              #      pass
                               # elif x == 0:
                                #    pass
                                #else:
                                 #   train_field.insert(i,functions.ToField(train_id,train_category,train_number,train_first_station,train_second_station,train_delay,train_speed))
                            
                    
                    functions.PrintField(train_field,i)
                    train_id += 1
                    i += 1
                    
                #Opakovanie do vyčerpania poľa
                while_counter += 1
                print("")
                print("Zoznam vlakov čakajúcich na spracovanie:")

                selected_id = int(input("Vyber si vlak, ktorý chceš odbaviť tým, že napíšeš jeho id: "))

                if level == 1:
                    selected_id -= 1

                #Ošetrenie nesprávne zadaného id-čka
                while field_lenght <= (selected_id):
                    print("Nevybral si správne vlak.")
                    selected_id = int(input("Vyber si vlak, ktorý chceš odbaviť tým, že napíšeš jeho id: "))
                
                #Premenné pre vybraný vlak
                selected_train = train_field[selected_id]
                train_category = selected_train['train_category']
                train_number = selected_train['train_number']
                train_first_station = selected_train['train_first_station']
                train_second_station = selected_train['train_second_station']

                train_station = functions.GetStations(train_category,train_first_station,train_second_station)

                #Poriešenie riešenia bez medziľahlých staníc
                if train_station == ['']:
                    print("Vlak ", train_category, train_number, " nemá žiadne medziľahlé stanice.")
                    time.sleep(1)
                    print("")
                    print("Teraz treba vybrať koľaje v jednotlivých staniciach, kde vlak zastavuje.")

                    #Výpis voľnosti koľají
                    print("Stanica ", train_second_station)
                    track_auto_number = 0
                    item = functions.GetItem(train_second_station)
                    Track(item,track_auto_number).StillFree(stations)
                    track_auto_number += 1
                else:
                    print("Medziľahlé stanice vlaku ", train_category, train_number, " sú: ", train_station)
                    time.sleep(1)
                    print("")
                    print("Teraz treba vybrať koľaje v jednotlivých staniciach, kde vlak zastavuje.")
                    print("")

                    #Výpis voľnosti koľají
                    for item in train_station:
                        if item == "..." or item == "Koš" or item == "Partizánske" or item == "Žilina-východ" or item == "Žilina-Hájik" or item == "Lučivná":
                            pass
                        else:
                            print("Stanica ", item)
                            track_auto_number = 0
                            item = functions.GetItem(item)
                            Track(item,track_auto_number).StillFree(stations)
                            track_auto_number += 1

                    print("Stanica ", train_second_station)
                    track_auto_number = 0
                    item = functions.GetItem(train_second_station)
                    Track(item,track_auto_number).StillFree(stations)
                    track_auto_number += 1

                if level <= 5 and (train_first_station == ['Tekovany'] or train_second_station == ['Tekovany']):
                    print("POZOR!!! V žst. Žilina musí ísť vlak na koľaj 6, 7 alebo 8!")

                print("")
                time.sleep(1)

                #Zadávanie koľají
                for item in train_station:
                    if item == 'Prievidza' or item == 'Nováky' or item == 'Žilina' or item == 'Čadca' or item == 'Kraľovany':
                        print("Koľaj v stanici ", item, ": ", end='')
                        track_number = int(input()) - 1

                        item = functions.GetItem(item)

                        Track(item,track_number).IsFree(stations)
                    elif item == "" or item == "...":
                        pass

                #Zadanie koľaje poslednej stanice
                if item == "Prievidza" or item == "Žilina" or item == "Čadca" or item == "Kraľovany":
                    print("Koľaj v konečnej stanici ", item,": ", end='')
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
                        train_second_station = functions.GetNameOfStation(item)

                        if train_second_station != train_second_station and train_second_station != "...":
                            Track(item,track_number).Sequence(train_category,train_number,stations)
                            
                    print(train_category, train_number, " prichádza do stanice ", train_second_station)

                train_field.pop(selected_id)

                score += 10

                if not train_field:
                    level += 1
                    while_counter = level
                    check.close()
                    os.remove("check.txt")   

                print(level)
                print(train_field)

            #GameOver
            if score < 0:
                print(user_name, " prehral si!")
                game = False
    else:
        user_name = input("Zadaj svoje meno, inak nebudeš hrať!: ")



