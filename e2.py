"""
Nom: Axel Garcia Hernandez, Axel Benitez Parra, Alex Jimenez Navarro
ASIXc 1A M03 UF1
Data: 22/01/2024
Descripció:
Programa que generi una llista de 100 nombres aleatoris entre 1 i 50. Obtenir la mitja dels nombres que es troben a les posicions parelles i la mitja del nombre de les posicions senars.
"""
import random

TOTALP = 50
TOTALS = 50
llista = []
mitjanaParells = 0
mitjanaSenars = 0

for i in range(100):
    num = random.randint(1,50)
    llista.append(num)
    if i % 2 == 0:
        mitjanaParells += num
    else:
        mitjanaSenars += num

mitjanaParells = mitjanaParells/TOTALP
mitjanaSenars = mitjanaSenars/TOTALS
llistaDef = [str(x) for x in llista]

print("Amb els nombres:", ", ".join(llistaDef))
print("Mitjana dels parells:",mitjanaParells)
print("Mitjana dels senars:",mitjanaSenars)