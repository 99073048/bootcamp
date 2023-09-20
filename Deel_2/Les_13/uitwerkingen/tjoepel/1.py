from tkinter import Variable


zin= "Hallo wereld dit is mijn zin"

#print(zin(2))

getal = 5
totaal=0

mijn_verzameling=  1,7,5,3,15,27,23,1#dit noem je een tjoepel

if getal in mijn_verzameling:
    print(f"het getal 15 zit er in")

for getal in mijn_verzameling:
 
 totaal = totaal+ getal 




naam_1= input("hoe heet heet je")
favoriete_kleur= input("wat is je favoriete kleur")

kleuren= ("rood,blauw,groen,paars,geel,oranje")


teken= len(naam_1)

print("{naam_1} bestaat uit {teken}")

   if favoriete_kleur in kleuren:
   print(f"wat een mooie kleur {naam_1} houdt van de kleur {favoriete_kleur}")

  else 
     print(f"deze print is niet zo mooi")

   # als je wil dat de gebruiker alleen lage letter gebruikt zet een lower achter het variabel favoriete_kleur.lower()