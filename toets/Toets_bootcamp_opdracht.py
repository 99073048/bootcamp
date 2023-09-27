# Opdracht 1 


# a: Waarom is Visual Studio Code handiger voor software development dan bijvoorbeeld Notepad Noem de voordelen!

# 1. je kan met visual studio code meerdere codetalen gebruiken en met notepad niet
# 2. je kan code schrijven die met een knop kan worden geëxecuteerd word

# b: Waarom is het goed dat je de commits van jouw code pusht naar github.com?
# # Zodat je kan terugkijken welke veranderingen er zijn gekomen met je bestand



# Opdracht 2:
# Maak het commentaar af.
a = 5  # dit is een voorbeeld van het datatype: integer
b = 10.5# dit is een voorbeeld van het datatype: float
c = "Hallo wereld" # dit is een voorbeeld van het datatype: string

 

# Opdracht 3:
# Schrijf code die de waarden van a en b omwisselt. Gebruik daarvoor een extra variabele.
a = 5
b = 10
a==b# voeg jouw code toe…

# Controleer met onderstaande code of de waarden correct zijn verwisseld
print(f"a = {a}, b = {b}") # Moet "a = 10 b = 5" printen



 

  

# Opdracht 4:

# Los de problemen op (zonder exception handling).

leeftijd = int(input("Hoe oud ben je?"))

if == 18:
   print(f"Dan duurt het nog ongeveer 67 - {leeftijd} jaar voordat je met pensioen mag!")

# Is 18 ingevuld? Dan zie je op de terminal: Dan duurt het nog ongeveer 49 jaar voordat je met pensioen mag!

 

# Opdracht 5: 
# Schrijf een functie die 3 getallen bij elkaar optelt en zorg ervoor
# dat de uitkomst ervan wordt getoond in de print
getal1 = 200
getal2 = 5
getal3 = 12
optellen = (getal1 + getal2 + getal3)# of de naam van je eigen functie.

print(f"De som van {getal1} + {getal2} + {getal3} = {optellen}")

 

# Opdracht 6:
# Maak de volgende code af:# Je moet bijbetalen als je over je minuten of je GB's heen gaat en geen onbeperkt abonnement hebt.

AANTAL_GB = 20 # Aantal GB data in je bundel
AANTAL_MINUTEN = 200 # Aantal belminuten in je bundel
ONBEPERKT = False # test ook met True
aantal_minuten_gebeld = int(input("Hoeveel minuten heb je gebeld?"))
aantal_GB_internet = int(input("Hoeveel GB's heb je gebruikt?"))

if aantal_minuten_gebeld > AANTAL_MINUTEN :
    print("Let op: je moet bijbetalen!")
else:
    print("Niet aan de hand gebruik je mobiel lekker verder!")

 

# Opdracht 7:
# Print onder elkaar de getallen 1-250 met max 2 regels code.
print("1")
print("250")


Opdracht 8:
# Gegeven is:

lijst_eten = ["appel", "pannenkoek", "kiwi", "hamburger","bananenijs","perenijs"]

print("het menu bevat")
print= (lijst_eten[0])
print= (lijst_eten[1])
print= (lijst_eten[2])
print= (lijst_eten[3])
print= (lijst_eten[4])
print= (lijst_eten[5])

teken= len() {lijst_eten}

if teken > lijst_eten:
   print(f"het {teken} heeft de meeste tekens")

# a: print een eenvoudig menu met de volgende layout:

# Onze menukaart:
# appel
# pannenkoek
# kiwi
# hamburger 

# b: Schrijf code die ervoor zorgt dat alleen het eten met de langste naam wordt geprint in de terminal. # Let op: je moet in de code eerst bepalen welk eten de langste naam heeft (en dus niet hardcoded 1 voor de index gebruiken). # test je code door extra eten toe te voegen met een nog langere naam.

 

Opdracht 9:
# Schrijf een programma wat de gebruiker vraagt een cijfer in te voeren via de terminal.
# Dit blijf je herhalen totdat de gebruiker een getal tussen 0 en 10 heeft ingevoerd.
# Voert de gebruiker iets anders in dan een getal: geef een foutmelding.

 




Opdracht 10:
# repareer de volgende code:
MAX= 20
getal = print("Voer een getal in")

MAX == 20:
if getal >= MAX:
   input(f"Het getal is groter dan [MAX]")
elif getal= MAX:
  input(f"Het getal is kleiner dan [MAX]")
else:
   input(f"Het getal is gelijk aan (MAX)")