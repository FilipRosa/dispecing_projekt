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
    elif train_category == ['R']:
        return random.randint(700, 719)

#funkcia pre random generovanie kategória vlaku
def GetTrainCategory(train_categories):
    return random.sample(train_categories, k = 1)

#funkcia pre random generovanie počiatočnej stanice vlaku
def GetTrainFirstStation(train_stations):
    return random.sample(train_stations, k = 1)

#funkcia pre random generovanie koncovej stanice vlaku
def GetTrainSecondStation(train_stations,train_first_station):
    return random.sample(train_stations, k = 1)

#funkcia pre random generovanie meškania vlaku
def GetTrainDelay(train_delays):
    return random.sample(train_delays, k = 1)

#funkcia pre vypísanie rýchlosti vlaku
def GetTrainSpeed(train_category):        
    return Speeds(train_category)  
        
#funkcia pre vypísanie čísla vlaku
def GetTrainNumber(train_category):
    return Numbers(train_category)

#funkcia pre vrátenie hodnoty item
def GetItem(item):
    if item == "Prievidza":
        return 0
    elif item == "Koš":
        return 1
    elif item == "Nováky":
        return 2
    elif item == "Partizánske":
        return 3
    elif item == "Žilina východ":
        return 4
    elif item == "Žilina":
        return 5
    elif item == "Žilina hájik":
        return 6
    elif item == "Tekovany":
        return 7
    elif item == "Lučivná":
        return 8
    elif item == "Čadca":
        return 9
    elif item == "Kraľovany":
        return 10
    elif item == "...":
        return 11

def GetNameOfStation(item):
    if item == 0:
        return "Prievidza"
    elif item == 1:
        return "Koš"
    elif item == 2:
        return "Nováky"
    elif item == 3:
        return "Partizánske"
    elif item == 4:
        return "Žilina východ"
    elif item == 5:
        return "Žilina"
    elif item == 6:
        return "Žilina hájik"
    elif item == 7:
        return "Tekovany"
    elif item == 8:
        return "Lučivná"
    elif item == 9:
        return "Čadca"
    elif item == 10:
        return "Kraľovany"
    elif item == 11:
        return "..."

def Sequence(train_category,train_number):
    print(train_category, train_number, " odišiel zo stanice ", )