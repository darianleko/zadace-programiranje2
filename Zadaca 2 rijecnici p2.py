import random

ucenici = ["Miro", "Stjepan", "Josip", "Toni", "Robert", "Marko", "Ljubo",
           "Josipa","Magdalena", "Ivana", "Stipe", "Emanuel", "Petar", "Ivan",
           "Luka","Filip","Lara", "Laura", "Mario", "Ana", "Marija", "Nikolina",
           "Andrija","Slaven","Sebastian", "Marko", "Frano", "Stipan", "Eugen",
           "Toni","Dražan", "Matej","Nives", "Nemanja", "Sara", "Ružica",
           "Gabrijel", "Darian","Ivana", "Ivan Stjepan","Kristian", "Josip",
           "Tomislav", "Jovan", "Gabrijel", "Mia","Ante", "Josip","Ante",
           "Josip", "Danijel", "Goran", "Zoran Ivan", "Franjo Francisko",
           "Sergej","Matej", "Marin", "Sara", "Josip", "Stjepan", "Iva",
           "Marko","Sara", "Krešimir","Magdalena", "Marko", "Mirko", "David",
           "Ema", "Paul", "Sven","Natalija",
           "Petar", "Emanuel", "Helena", "Antonio", "Petar"]

rij=dict()
print(len(ucenici))

for ucenik in ucenici:
    rij[ucenik]=random.randint(1,5)
print(len(rij))
print(rij)


broj_ocj=dict()
for i in rij.values():
    if i in broj_ocj:
        broj_ocj[i]+=1
    else:
        broj_ocj[i]=1
print(broj_ocj)
brojac=0
for ocjena in rij.values():
    if ocjena>1:
        brojac+=1
print("Broj ucenika s pozitivnom ocjenom:" , brojac)

prolaznost=brojac/len(ucenici)*100
print("Prolaznost je",prolaznost, "%")
