
# # Houd rekening met het volgende:
# # Je schrijft een programma met 1 variabele: cijfer. Dit cijfer gebruik je om de omschrijving te printen:

# Controleer het ingevoerde cijfer en druk de bijbehorende omschrijving af
# Vraag de gebruiker om een cijfer tussen 1 en 10 in te voeren

cijfer = float(input("Voer een cijfer tussen 1 en 10 in: "))

# Controleer of het ingevoerde cijfer binnen het juiste bereik ligt
if cijfer < 1 or cijfer > 10:
    print("Dit kan ik niet omzetten!")
else:
    # Maak een lege variabele om de omschrijving op te slaan
    omschrijving = ""

    # Bepaal de omschrijving op basis van het ingevoerde cijfer
    if cijfer == 10:
        omschrijving = "uitmuntend"
    elif cijfer == 9:
        omschrijving = "zeer goed"
    elif cijfer == 8:
        omschrijving = "goed"
    elif cijfer == 7:
        omschrijving = "ruim voldoende"
    elif cijfer == 6:
        omschrijving = "voldoende"
    elif cijfer == 5:
        omschrijving = "bijna voldoende"
    elif cijfer == 4:
        omschrijving = "onvoldoende"
    elif cijfer == 3:
        omschrijving = "gering"
    elif cijfer == 2:
        omschrijving = "slecht"
    elif cijfer == 1:
        omschrijving = "zeer slecht"

    # Controleer of het cijfer 6 of groter is en geef de juiste boodschap weer
    if cijfer >= 6:
        print(f"Gefeliciteerd, {omschrijving} je resultaat is een {cijfer}")
    else:
        print(f"Jammer, {omschrijving} je resultaat is een {cijfer}")


# Cijfer	Omschrijving
# 10	uitmuntend
# 9	zeer goed
# 8	goed
# 7	ruim voldoende
# 6	voldoende
# 5	bijna voldoende
# 4	onvoldoende
# 3	gering
# 2	slecht
# 1	= zeer slecht