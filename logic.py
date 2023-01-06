from trains import Train
from dispatcher import Dispatcher

user_name = input("Zadaj svoje meno: ")

print("Ahoj " + user_name + " vitaj na pracovisku vlakového dispečingu pre trať Prievidza - Kraľovany!")

prievidza = [True, True, True, True, True, True]
kos = [True]
novaky = [True, True, True]
partizanske = [True]
zilina_vychod = [True]
zilina = [True, True, True, True, True, True, True, True]
zilina_hajik = [True]
tekovany = [True]
lucivna = [True, True]
cadca = [True, True, True, True]
kralovany = [True, True]

train = Train("IC","Prievidza - Čadca",0,60)

dispatcher = Dispatcher()
dispatcher.add_train(train)
dispatcher.dellay_all_trains(15)

print(train.name)
print(train.route)
print(train.position)
print(train.speed)