# Opdracht 1:
# Schrijf een programma dat een lege lijst maakt en vervolgens de gebruiker vraagt om 5 getallen in te voeren. Gebruik de append functie om elk getal aan de lijst toe te voegen en print vervolgens de lijst.
# Maak een lege lijst
getallen_lijst = []

# Vraag de gebruiker om 5 getallen in te voeren en voeg ze toe aan de lijst
for i in range(5):
    getal = float(input(f"Voer getal {i+1} in: "))  # We gebruiken float() om ervoor te zorgen dat de invoer als een getal wordt behandeld
    getallen_lijst.append(getal)

# Druk de lijst af
print("De ingevoerde getallen zijn:")
print(getallen_lijst)
