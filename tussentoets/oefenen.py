
# vraag de gebruikers naam
naam=input("voer uw naam hier in:")


# vraag de gebruiker om zijn leeftijd
leeftijd= int (input("voer uw leeftijd in"))

if leeftijd >= 18:
 print("ja")
elif leeftijd >18 and leeftijd >0:
 print("nee u mag niet verder")

else: 
 print("ongeldige leeftijd")

#hier gebruik je de "and" operator waardoor je zegt dat "leeftijd" ook groter dan 0 moet zijn.

# elif leeftijd >18 and leeftijd >0: