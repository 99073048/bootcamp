import from 

def get_integer(vraag):
    while True:
        try:
            leeftijd = int(input(vraag))
            return leeftijd
        except ValueError:
            print("Ongeldige invoer. Voer een geheel getal in.")

def get_float(vraag):
    while True:
        try:
            getal = float(input(vraag))
            return getal
        except ValueError:
            print("Ongeldige invoer. Voer een getal in.")

# herhaalde vragen
leeftijd = get_integer("Wat is je leeftijd? ")
print(f"Je bent {leeftijd} jaar oud.")

getal = get_float("Voer een getal in: ")
print(f"Het ingevoerde getal is: {getal}")


# Opdracht 1:
# Pak opdracht 3 van gisteren.
# Kijk eens naar de functies: get_integer en get_float.
# Voer hier eens een string (bijv.: zes) in! Wat gebeurt er?
# Los dit probleem op met een try en except.

# Let op: Zorg ervoor dat je net zolang om een getal vraagt tot de gebruiker een geldig getal heeft ingevoerd.

