# Prijzen van het fruit
prijs_appels = 3.40
prijs_druiven = 2.45
prijs_bananen = 1.95

# Bereken de totale prijs van het fruit
totale_prijs = prijs_appels + prijs_druiven + prijs_bananen

# BTW-tarief
btw_tarief = 9

# Bereken de BTW
btw_bedrag = totale_prijs * (btw_tarief / 100)

# Print de resultaten
print("Totale prijs van het fruit: €", totale_prijs)
print("BTW-bedrag: €", btw_bedrag)