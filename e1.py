"""
Nom: Axel Garcia Hernandez, Axel Benitez Parra, Alex Jimenez Navarro
ASIXc 1A M03 UF1
Data: 22/01/2024
Descripció:
Fer un programa de càlcul de temperatures del mar. Les tasques a fer són:
Calcular per a l’any 2022: temperatura màxima, mínima i mitjana
Calcular per període 2000 a 2022: temperatura màxima, mínima i mitjana
"""

data = [
    [13.6, 13.4, 13.2, 13.4, 13.9, 13.7, 13.7, 13.8, 14, 14.3, 16, 15.1, 14],
    [13.3, 12.9, 13.5, 13.5, 13.7, 13.8, 13.8, 13.8, 14.2, 14.6, 16.8, 14.7, 14.1],
    [14.4, 13.9, 13.6, 13.5, 13.7, 13.9, 13.9, 14, 14.3, 14.7, 15.6, 14.6, 14.2],
    [13.9, 12.5, 13.3, 13.4, 14, 13.9, 13.8, 13.9, 14.5, 14.9, 15.5, 15.4, 14.1],
    [13.2, 12.7, 12.3, 12.9, 13.8, 13.9, 14, 14.1, 14.3, 17.9, 17.7, 15.9, 14.4],
    [13.7, 12.8, 13.4, 13.9, 14, 14, 13.9, 14, 14, 14.6, 14.8, 13.3, 13.9],
    [14.1, 13.6, 12.9, 13.5, 14, 13.9, 14, 14, 14.2, 16.3, 16.5, 15.6, 14.4],
    [14.1, 12.6, 12.9, 13.5, 14.3, 13.9, 13.7, 13.8, 14.1, 15.8, 15.8, 15.1, 14.1],
    [13.7, 13.2, 13.6, 13.6, 14.7, 14.2, 13.9, 14, 14.5, 15.7, 16.5, 16, 14.5],
    [13.2, 12.2, 12, 13.1, 13.5, 14.1, 13.7, 13.6, 13.6, 15.3, 15.9, 13.6, 13.7],
    [13.9, 12.4, 12.6, 13.3, 13.7, 13.5, 13.5, 13.7, 13.9, 14.8, 15.8, 13.9, 13.8],
    [13, 12.5, 12.5, 13.6, 13.5, 14, 14.1, 13.7, 13.8, 15.2, 17.6, 15.9, 14.1],
    [12.6, 11.9, 12.2, 12.8, 13.7, 13.6, 13.5, 13.5, 13.9, 15.6, 15.5, 14, 13.6],
    [13.3, 12.5, 12.6, 12.8, 14.2, 13.7, 13.7, 13.8, 14, 16.2, 15.9, 14.5, 13.9],
    [13.2, 13, 12.9, 12.8, 13.3, 13.6, 13.7, 13.8, 13.9, 14.3, 15.5, 13.8, 13.7],
    [14.3, 13.4, 13.2, 13.4, 14.4, 13.8, 13.8, 13.8, 14, 15.5, 15.5, 13.9, 14.1],
    [12.5, 12.3, 12.1, 12.9, 13.1, 13.4, 13.2, 13.2, 14, 15.5, 17.3, 15.8, 13.8],
    [13.3, 12.3, 12.3, 12.9, 13.4, 13.3, 13.3, 13.4, 13.9, 15.2, 17.1, 14.4, 13.7],
    [13.5, 12.7, 12.3, 12.6, 13.2, 13.1, 13.3, 13.6, 14.9, 15.3, 15.4, 14.6, 13.7],
    [13.6, 12.2, 12.5, 12.8, 14.7, 13.5, 13.6, 13.7, 14.2, 15.9, 15.3, 15, 13.9],
    [13.2, 12.4, 12.9, 13.4, 13.7, 13.6, 14.4, 13.8, 14.3, 14.8, 15.3, 14.2, 13.8],
    [13.8, 13, 12.6, 13.6, 13.5, 13.4, 14, 14, 14.2, 15.3, 16.8, 14, 14],
    [12.7, 12.4, 12.6, 12.4, 13, 13.6, 13.3, 13.6, 13.5, 15.9, 15.3, 14.9, 13.6]
]
"""
first_year = list(data.keys())[0]
values_of_first_year = data[first_year]

for value in values_of_first_year:
    print(value, end=" ")
"""
suma = 0
for i in data:
    for x in data:
        suma = suma + data[i][x]


print(suma)