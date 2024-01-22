"""
Nom: Axel Garcia Hernandez, Axel Benitez Parra, Alex Jimenez Navarro
ASIXc 1A M03 UF1
Data: 22/01/2024
Descripció:
Programa que generi una llista de 100 nombres aleatoris entre 1 i 50. Obtenir la mitja dels nombres que es troben a les posicions parelles i la mitja del nombre de les posicions senars.
"""
llista = []
mitjanaParells = 0
mitjanaSenars = 0
import random
for i in range(100):
    num = random.randint(1,50)
    llista.append(num)
    if i % 2 == 0:
        mitjanaParells += num
    else:
        mitjanaSenars += num

print(llista)
print("Mitjana dels parells:",mitjanaParells/50)
print("Mitjana dels senars:",mitjanaSenars/50)