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

#funkcia pre random generovanie kategória vlaku
def GetTrainCategory(train_categories):
    return random.sample(train_categories, k = 1)

#funkcia pre random generovanie počiatočnej stanice vlaku
def GetTrainFirstStation(train_stations):
    return random.sample(train_stations, k = 1)

#funkcia pre random generovanie koncovej stanice vlaku
def GetTrainSecondStation(train_stations):
    station = random.sample(train_stations, k = 1)

    if GetTrainFirstStation(train_stations) == station:
        station = random.sample(train_stations, k = 1)
    else:
        return station

#funkcia pre random generovanie meškania vlaku
def GetTrainDelay(train_delays):
    return random.sample(train_delays, k = 1)

#funkcia pre vypísanie rýchlosti vlaku
def GetTrainSpeed(train_category):        
    return Speeds(train_category)  
        
#funkcia pre vypísanie čísla vlaku
def GetTrainNumber(train_category):
    return Numbers(train_category)

#funkcia na zistenie voľnosti koľaje
def IsFree(item,track_number):
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
        
    if stations[item][track_number] == True:
        stations[item][track_number] = False
        print("Žiadosť o obsadenie koľaje úspešná.")
    elif stations[item][track_number] == False:
        print("Koľaj obsadená.")