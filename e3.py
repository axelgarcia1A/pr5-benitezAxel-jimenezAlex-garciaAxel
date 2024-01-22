"""
Nom: Axel Garcia Hernandez, Axel Benitez Parra, Alex Jimenez Navarro
ASIXc 1A M03 UF1
Data: 22/01/2024
Descripció:
Programa de traducció d’insults. Crear una estructura de dues dimensions amb els insults en català i afegir la traducció en castellà, anglès i klingon
"""

insults = {
    "CAT": ["carallot", "mocos", "malparit", "tros de quoniam", "flasca", "llondro", "abraçafanals"],
    "ESP": ["empanado", "mocoso", "malparido", "tonto", "vago", "idiota", "pelotero"],
    "ANG": ["tarnished", "punk", "bastard", "silly", "lazy", "moron", "ass licker"],
    "KLN": ["sep", "yiv", "marqeq", "dogh", "qo'", "petaq", "daH ngab"]
}

user = input("Dime un insulto: ").lower()

if user in insults["CAT"]:
    posicion = insults["CAT"].index(user)
    print(insults["ESP"][posicion])
    print(insults["ANG"][posicion])
    print(insults["KLN"][posicion])

elif user in insults["ESP"]:
    posicion = insults["ESP"].index(user)
    print(insults["CAT"][posicion])
    print(insults["ANG"][posicion])
    print(insults["KLN"][posicion])

elif user in insults["ANG"]:
    posicion = insults["ANG"].index(user)
    print(insults["CAT"][posicion])
    print(insults["ESP"][posicion])
    print(insults["KLN"][posicion])

elif user in insults["KLN"]:
    posicion = insults["KLN"].index(user)
    print(insults["CAT"][posicion])
    print(insults["ESP"][posicion])
    print(insults["ANG"][posicion])
else:
    print("Insulto no disponible")
