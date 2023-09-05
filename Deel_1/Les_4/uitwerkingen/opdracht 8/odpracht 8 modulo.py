# Schrijf een programma wat uitrekent hoeveel keer 13 (helemaal) in 625 past!
# Bereken ook wat er overblijft.
# (hint: gebruik de modulo en integer deling (of floor division))
# Getal waarin we willen delen
totaal = 625

# Getal dat we willen delen
deeltal = 13

# Bereken hoe vaak deeltal in totaal past
aantal_keer = totaal // deeltal 


# berekening wat er overblijft met modulo 

rest = totaal % deeltal

print (f" {deeltal} past {aantal_keer}keer in {totaal}." )

print (f"er blijft {rest} over.")

