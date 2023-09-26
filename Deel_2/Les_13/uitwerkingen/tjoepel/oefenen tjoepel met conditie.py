# kleuren = ["rood", "blauw", "groen", "geel"]
# favoriete_kleur = "blauw"
# naam_1 = "Jan"

# if favoriete_kleur in kleuren:
#     print(f"wat een mooie kleur {naam_1} houdt van de kleur {favoriete_kleur}")
# else:
#     print("deze kleur is niet in de lijst van favoriete kleuren")

# from tkinter import Variable

# # het begin 
# zin= "Hallo wereld dit is mijn zin"

# print(zin(2))

# getal = 5
# totaal=0

# mijn_verzameling=  1,7,5,3,15,27,23,1#dit noem je een tjoepel

# if getal in mijn_verzameling:
#     print(f"het getal 15 zit er in")

# for getal in mijn_verzameling:
 
#  totaal = totaal+ getal 

naam_1 = input("Hoe heet je? ")
favoriete_kleur = input("Wat is je favoriete kleur? ")

kleuren = ("rood,blauw,groen,paars,geel,oranje")  # Dit noem je een tuple 

teken = len(naam_1)

print(f"{naam_1} bestaat uit {teken} tekens")  # Gebruik f-strings om variabelen in te voegen

if favoriete_kleur.lower() in kleuren:  # Gebruik .lower() om de invoer in kleine letters te converteren
    print(f"Wat een mooie kleur! {naam_1} houdt van de kleur {favoriete_kleur}.")
else:
    print("wat jammer dAT IS NIET ZO MOOI")
    