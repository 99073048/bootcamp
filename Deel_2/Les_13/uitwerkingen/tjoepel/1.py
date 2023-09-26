

    
naam_1 = input("Hoe heet je? ")
favoriete_kleur = input("Wat is je favoriete kleur? ")

kleuren = ("rood,blauw,groen,paars,geel,oranje")  # Dit noem je een tuple

teken = len(naam_1)

print(f"{naam_1} bestaat uit {teken} tekens")  # Hier moet je f-string gebruiken om de variabelen in te voegen

if favoriete_kleur.lower() in kleuren:  # Gebruik .lower() om de invoer in kleine letters te converteren
    print(f"Wat een mooie kleur! {naam_1} houdt van de kleur {favoriete_kleur}.")
else:
    print("Deze kleur is niet zo mooi.")

   
# if favoriete_kleur.lower() in kleuren:
#    print(f"wat een mooie kleur {naam_1} houdt van de kleur {favoriete_kleur}.")
# else:
#    print("deze kleur is niet in de lijst van favoriete kleuren")
   # als je wil dat de gebruiker alleen lage letter gebruikt zet een lower achter het variabel favoriete_kleur.lower()

