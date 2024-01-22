"""
Nom: Axel Garcia Hernandez, Axel Benitez Parra, Alex Jimenez Navarro
ASIXc 1A M03 UF1
Data: 22/01/2024
Descripció:
Programa que generi una llista de 100 nombres aleatoris entre 1 i 50. Obtenir la mitja dels nombres que es troben a les posicions parelles i la mitja del nombre de les posicions senars.
"""
llista = []
parells = []
senars = []
mitjanaParells = 0
mitjanaSenars = 0
totalP = 0
totalS = 0
import random
for i in range(100):
    num = random.randint(1,50)
    llista.append(num)
    if num % 2 == 0:
        parells.append(num)
        totalP += 1
    elif num % 2 != 0:
        senars.append(num)
        totalS += 1
for x in parells:
    mitjanaParells = mitjanaParells + x

for x in senars:
    mitjanaSenars = mitjanaSenars + x

print("Mitjana dels parells:",mitjanaParells/totalP)
print("Mitjana dels senars:",mitjanaSenars/totalS)