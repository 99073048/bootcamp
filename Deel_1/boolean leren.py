

# b.
# De BTW voor al het fruit in de fruitmand: 
# je betaalde 3.40 euro voor de appels, 
# 2.45 voor de druiven, 
# 1.95 voor de bananen. 

# En By The Way wat is de BTW op fruit? 9%!


# Prijzen van de verschillende fruitsoorten
prijs_appels = 3.40
prijs_druiven = 2.45
prijs_bananen = 1.95

# BTW-tarief (9%)
btw_tarief = 0.09

# bedrag zonder btw
totaalbedrag_zonder_btw = prijs_appels + prijs_druiven + prijs_bananen

# Het btw bedrag
btw_bedrag= totaalbedrag_zonder_btw * btw_tarief

# bedrag inclusief btw 
bedrag_met_btw= btw_bedrag+totaalbedrag_zonder_btw 

----------------------------------------------------------

# Maak een variabele "naam" en geef deze je eigen naam als waarde
naam = "JouwNaam"

# Schrijf een statement om de boodschap af te drukken
print("Hallo " + naam + ", ik leer nu programmeren.")

# In dit programma worden de volgende operators gebruikt:
# =: De toekenningsoperator wordt gebruikt om de waarde "JouwNaam" aan de variabele "naam" toe te wijzen.
# +: De concatenatieoperator wordt gebruikt om de strings samen te voegen en de boodschap af te drukken.
# Om de waarde van "naam" te veranderen naar de naam van je buurman, hoef je alleen de waarde aan te passen:

--------------------------------------------------------------
# Maak een variabele "naam" en geef deze de waarde 252
naam = 252  # De variabele "naam" is nu van het type 'int' (integer).

# Schrijf een statement om de boodschap af te drukken
1.  print("Hallo " + str(naam) + ", ik leer nu programmeren.")

2.  print ("de punten dat ik heb gekregen is"+ str(naam)+ "is dat niet cool")

# str()-functie om het getal om te zetten naar een string, 
# zodat het kan worden samengevoegd met de tekst en afgedrukt.

---------------------------------------------------------------

# Opdracht 5:
# Schrijf een programma met twee variabelen.
# Geef de eerste variabele de waarde 25 en de tweede 0.
# Deel variabele een door variabele twee. 
# Wat gebeurt er? 

een = 25
twee = 0

resultaat = een / twee  # Dit zal een ZeroDivisionError veroorzaken doordat de waarde 0 nergens mee kan delen
------------------------------------------------
# Opdracht 6:
# Zit er een fout in de haakjes? Los deze op!: 
print (((2*3 /4) + (5 -6/7) *8 )) # We verwachten: 34.642857142857146
print( ((12*13 /14) + (15 -16) /17) *18 ) # We verwachten: 199.5126050420168
-------------------------------------------------
# opdracht 7
resultaat = (431 / 100) * 100
print(float (resultaat))

-------------------------------------------------

# Opdracht 8:
# Schrijf een programma wat uitrekent hoeveel keer 13 (helemaal) in 625 past!
# Bereken ook wat er overblijft.
# (hint: gebruik de modulo en integer deling (of floor division))
# Definieer de gegevens
totaal = 625
deler = 13

# Bereken hoeveel keer de deler in het totaal past (integer deling)
aantal_keer = totaal // deler

# Bereken wat er overblijft na deling (modulo)
overblijft = totaal % deler

# Toon de resultaten
print(f"{totaal} past {aantal_keer} keer in {deler} met een rest van {overblijft}.")

------------------------------------------------------------------------
# integer en f" gaan samen

# hoeveel de deler in het totaal past 
aantal_delingen= totaal // deler

# Modulo
overblijft_na_deling= totaal % deler

print(f" het totaal {totaal}past {aantal_delingen} met de {deler} en er blijft {overblijft_na_deling} over ")


%  wat overblijft na deling
-----------------------------------------------------------------
# User
# Opdracht 3:
# Definieer drie variabelen var1, var2 en var3. Bereken het gemiddelde en
# stop het in een variabele gemiddelde. Toon het gemiddelde. Voeg drie commentaren toe.
# Pas het programma nu zo aan dat de gebruiker getallen kan invoeren

# Vraag de gebruiker om invoer voor var1, var2 en var3
var1 = float(input("Voer het eerste getal in: "))
var2 = float(input("Voer het tweede getal in: "))
var3 = float(input("Voer het derde getal in: "))

# Bereken het gemiddelde van de ingevoerde getallen
gemiddelde = (var1 + var2 + var3) / 3

# Toon het berekende gemiddelde
print("Het gemiddelde van de ingevoerde getallen is:", gemiddelde)

----------------

var1=float(input)("voer het eerste getal in")
var2=float(input)("voer het tweede getal in")
var3=float(input)("voer het derde getal in")

gemiddelde= (var1 +var2+var3)/3

print("Het gemiddelde van alle variabelen is" {gemiddelde} )
-----------------------------------------------------

# De fout in deze code is het gebruik van het enkele gelijkteken (=) 
# in plaats van de dubbele gelijktekens (==) binnen de if-verklaring. 
# In Python wordt de enkele gelijkteken gebruikt om een waarde aan een variabele toe te kennen,
# terwijl de dubbele gelijktekens worden gebruikt om te controleren of twee waarden gelijk zijn. 
# Hier is de gecorrigeerde versie van de code:

if x == 18:
    print('de waarde van x = 18')

----------------------------------------------------


 a = 3
 b = 7

if a > b:
   print("Variabele a is het grootst want {a} is groter dan {b} ")
elif b > a
   print("Variabele {b} is het grootst want {b} is groter dan {waarde a}")
else: 
   print("de variabelen zijn helaas gelijk ")

-------------------------------------

# Definieer de variabele leeftijd
leeftijd = int(input("Voer je leeftijd in: "))


# Controleer of de leeftijd 16 of hoger is
if leeftijd >= 16:
    print("Gefeliciteerd, je mag je brommerrijbewijs halen.")
else:
    print("Helaas, je zult nog even moeten wachten.")

----------------------------------------