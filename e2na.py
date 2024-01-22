"""
Nom: Axel Garcia Hernandez, Axel Benitez Parra, Alex Jimenez Navarro
ASIXc 1A M03 UF1
Data: 22/01/2024
Descripció:
Programa que calcula la suma dels dígits parells d'un número positiu.
"""

numero = int(input())

div = numero % 2

if div == 0:
    print("es parell")
else:
    print("no es parell")