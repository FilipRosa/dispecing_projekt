from trains import Train
from dispatcher import Dispatcher
import random

#funkcia pre random generovanie rýchlosti
def Speeds(train_category):
    if train_category == ['Os']:
        return random.randint(40, 100)
    elif train_category == ['Zr']:
        return random.randint(80, 120)
    else:
        return random.randint(80, 140)

#funkcia pre random generovanie čísla vlaku
def Numbers(train_category):
    if train_category == ['Os']:
        return random.randint(5000, 5099)
    elif train_category == ['Zr']:
        return random.randint(1880, 1889)
    else:
        return random.randint(700, 719)

#funkcia pre určenie medziľahlých staníc vlaku
def GetStations(train_category,train_first_station,train_second_station):
    #osobný vlak
    if train_category == ['Os']:
        if train_first_station == ['Prievidza']:
            if train_second_station == ['Čadca']:
                return ['Koš','Nováky','Partizánske','Žilina-východ','Žilina','Lučivná']
            elif train_second_station == ['Žilina']:
                return ['Koš','Nováky','Partizánske','Žilina-východ']
            elif train_second_station == ['Kraľovany']:
                return ['Koš','Nováky','Partizánske','Žilina-východ','Žilina','Lučivná','Čadca']
            elif train_second_station == ['...']:
                return ['Koš','Nováky','Partizánske','Žilina-východ','Žilina','Lučivná','Čadca','Kraľovany']
            elif train_second_station == ['Tekovany']:
                return ['Koš','Nováky','Partizánske','Žilina-východ','Žilina','Žilina-Hájik']
        elif train_first_station == ['Žilina']:
            if train_second_station == ['Čadca']:
                return ['Lučivná']
            elif train_second_station == ['Prievidza']:
                return ['Žilina-východ','Partizánske','Nováky','Koš']
            elif train_second_station == ['Kraľovany']:
                return ['Lučivná','Čadca']
            elif train_second_station == ['...']:
                return ['Lučivná','Čadca','Kraľovany']
            elif train_second_station == ['Tekovany']:
                return ['Žilina-Hájik']
        elif train_first_station == ['Čadca']:
            if train_second_station == ['Žilina']:
                return ['Lučivná']
            elif train_second_station == ['Prievidza']:
                return ['Lučivná','Žilina','Žilina-východ','Partizánske','Nováky','Koš']
            elif train_second_station == ['Kraľovany']:
                return ['']
            elif train_second_station == ['...']:
                return ['Kraľovany']
            elif train_second_station == ['Tekovany']:
                return ['Lučivná','Žilina','Žilina-Hájik']
        elif train_first_station == ['Kraľovany']:
            if train_second_station == ['Žilina']:
                return ['Čadca','Lučivná']
            elif train_second_station == ['Prievidza']:
                return ['Čadca','Lučivná','Žilina','Žilina-východ','Partizánske','Nováky','Koš']
            elif train_second_station == ['Čadca']:
                return ['']
            elif train_second_station == ['...']:
                return ['']
            elif train_second_station == ['Tekovany']:
                return ['Čadca','Lučivná','Žilina','Žilina-Hájik']
        elif train_first_station == ['...']:
            if train_second_station == ['Žilina']:
                return ['Kraľovany','Čadca','Lučivná']
            elif train_second_station == ['Prievidza']:
                return ['Kraľovany','Čadca','Lučivná','Žilina','Žilina-východ','Partizánske','Nováky','Koš']
            elif train_second_station == ['Čadca']:
                return ['Kraľovany']
            elif train_second_station == ['Kraľovany']:
                return ['']
            elif train_second_station == ['Tekovany']:
                return ['Kraľovany','Čadca','Lučivná','Žilina','Žilina-Hájik']
        elif train_first_station == ['Tekovany']:
            if train_second_station == ['Žilina']:
                return ['Žilina-Hájik']
            elif train_second_station == ['Prievidza']:
                return ['Žilina-Hájik','Žilina','Žilina-východ','Partizánske','Nováky','Koš']
            elif train_second_station == ['Čadca']:
                return ['Žilina-Hájik','Žilina','Lučivná']
            elif train_second_station == ['Kraľovany']:
                return ['Žilina-Hájik','Žilina','Lučivná','Čadca']
            elif train_second_station == ['...']:
                return ['Žilina-Hájik','Žilina','Lučivná','Čadca','Kraľovany']   
    #zrýchlený vlak    
    elif train_category == ['Zr']:
        if train_first_station == ['Prievidza']:
            if train_second_station == ['Čadca']:
                return ['Nováky','Partizánske','Žilina-východ','Žilina']
            elif train_second_station == ['Žilina']:
                return ['Nováky','Partizánske','Žilina-východ']
            elif train_second_station == ['Kraľovany']:
                return ['Nováky','Partizánske','Žilina-východ','Žilina','Čadca']
            elif train_second_station == ['...']:
                return ['Nováky','Partizánske','Žilina-východ','Žilina','Čadca','Kraľovany']
            elif train_second_station == ['Tekovany']:
                return ['Nováky','Partizánske','Žilina-východ','Žilina']
        elif train_first_station == ['Žilina']:
            if train_second_station == ['Čadca']:
                return ['']
            elif train_second_station == ['Prievidza']:
                return ['Žilina-východ','Partizánske','Nováky']
            elif train_second_station == ['Kraľovany']:
                return ['Čadca']
            elif train_second_station == ['...']:
                return ['Čadca','Kraľovany']
            elif train_second_station == ['Tekovany']:
                return ['']
        elif train_first_station == ['Čadca']:
            if train_second_station == ['Žilina']:
                return ['']
            elif train_second_station == ['Prievidza']:
                return ['Žilina','Žilina-východ','Partizánske','Nováky']
            elif train_second_station == ['Kraľovany']:
                return ['']
            elif train_second_station == ['...']:
                return ['Kraľovany']
            elif train_second_station == ['Tekovany']:
                return ['Žilina']
        elif train_first_station == ['Kraľovany']:
            if train_second_station == ['Žilina']:
                return ['Čadca']
            elif train_second_station == ['Prievidza']:
                return ['Čadca','Žilina','Žilina-východ','Partizánske','Nováky']
            elif train_second_station == ['Čadca']:
                return ['']
            elif train_second_station == ['...']:
                return ['']
            elif train_second_station == ['Tekovany']:
                return ['Čadca','Žilina']
        elif train_first_station == ['...']:
            if train_second_station == ['Žilina']:
                return ['Kraľovany','Čadca']
            elif train_second_station == ['Prievidza']:
                return ['Kraľovany','Čadca','Žilina','Žilina-východ','Partizánske','Nováky']
            elif train_second_station == ['Čadca']:
                return ['Kraľovany']
            elif train_second_station == ['Kraľovany']:
                return ['']
            elif train_second_station == ['Tekovany']:
                return ['Kraľovany','Čadca','Žilina']
        elif train_first_station == ['Tekovany']:
            if train_second_station == ['Žilina']:
                return ['']
            elif train_second_station == ['Prievidza']:
                return ['Žilina','Žilina-východ','Partizánske','Nováky']
            elif train_second_station == ['Čadca']:
                return ['Žilina']
            elif train_second_station == ['Kraľovany']:
                return ['Žilina','Čadca']
            elif train_second_station == ['...']:
                return ['Žilina','Čadca','Kraľovany']
    #rýchlik   
    elif train_category == ['R']:
        if train_first_station == ['Prievidza']:
            if train_second_station == ['Čadca']:
                return ['Partizánske','Žilina']
            elif train_second_station == ['Žilina']:
                return ['Partizánske']
            elif train_second_station == ['Kraľovany']:
                return ['Partizánske','Žilina','Čadca']
            elif train_second_station == ['...']:
                return ['Partizánske','Žilina','Čadca','Kraľovany']
            elif train_second_station == ['Tekovany']:
                return ['Partizánske','Žilina']
        elif train_first_station == ['Žilina']:
            if train_second_station == ['Čadca']:
                return ['']
            elif train_second_station == ['Prievidza']:
                return ['Partizánske']
            elif train_second_station == ['Kraľovany']:
                return ['Čadca']
            elif train_second_station == ['...']:
                return ['Čadca','Kraľovany']
            elif train_second_station == ['Tekovany']:
                return ['']
        elif train_first_station == ['Čadca']:
            if train_second_station == ['Žilina']:
                return ['']
            elif train_second_station == ['Prievidza']:
                return ['Žilina','Partizánske']
            elif train_second_station == ['Kraľovany']:
                return ['']
            elif train_second_station == ['...']:
                return ['Kraľovany']
            elif train_second_station == ['Tekovany']:
                return ['Žilina']
        elif train_first_station == ['Kraľovany']:
            if train_second_station == ['Žilina']:
                return ['Čadca']
            elif train_second_station == ['Prievidza']:
                return ['Čadca','Žilina','Partizánske']
            elif train_second_station == ['Čadca']:
                return ['']
            elif train_second_station == ['...']:
                return ['']
            elif train_second_station == ['Tekovany']:
                return ['Čadca','Žilina']
        elif train_first_station == ['...']:
            if train_second_station == ['Žilina']:
                return ['Kraľovany','Čadca']
            elif train_second_station == ['Prievidza']:
                return ['Kraľovany','Čadca','Žilina','Partizánske']
            elif train_second_station == ['Čadca']:
                return ['Kraľovany']
            elif train_second_station == ['Kraľovany']:
                return ['']
            elif train_second_station == ['Tekovany']:
                return ['Kraľovany','Čadca','Žilina']
        elif train_first_station == ['Tekovany']:
            if train_second_station == ['Žilina']:
                return ['']
            elif train_second_station == ['Prievidza']:
                return ['Žilina','Partizánske']
            elif train_second_station == ['Čadca']:
                return ['Žilina']
            elif train_second_station == ['Kraľovany']:
                return ['Žilina','Čadca']
            elif train_second_station == ['...']:
                return ['Žilina','Čadca','Kraľovany']       

user_name = input("Zadaj svoje meno: ")

print("Ahoj " + user_name + ", vitaj na pracovisku vlakového dispečingu pre trať Prievidza - Kraľovany!")
print("")
print("Zoznam vlakov čakajúcich na spracovanie:")
print("Id:     Kategória:     Číslo:     Počiatočná stanica:     Konečná stanica:     Meškanie:     Max.rýchlosť:")

i = 0

train_categories = ["Os","Zr","R"]
train_stations = ["Prievidza","Žilina","Čadca","Kraľovany","Tekovany","..."]
train_delays = [0, 5, 10]

while i < 1:
    train_id = i
    train_category = random.sample(train_categories, k = 1)
    train_first_station = random.sample(train_stations, k = 1)
    train_second_station = random.sample(train_stations, k = 1)
    train_delay = random.sample(train_delays, k = 1)
    train_speed = Speeds(train_category)
    train_number = Numbers(train_category)

    if train_first_station == train_second_station:
        train_second_station = random.sample(train_stations, k = 1)

    print(f"{str(train_id + 1):<10}{str(train_category):<15}{str(train_number):<15}{str(train_first_station):<25}{str(train_second_station):<20}{str(train_delay):<20}{str(train_speed)}")

    i += 1

print("")
user_select = input("Vyber si vlak, ktorý chceš odbaviť tým, že napíšeš jeho id: ")
