# opdracht 3
# vraag de gebruikers naam
naam=input("voer uw naam hier in:")


# vraag de gebruiker om zijn leeftijd
leeftijd= int (input("voer uw leeftijd in"))

if leeftijd < 18:
   print (f" Beste {naam}, je bent nog geen 18. Alleen autorijden zit er dus niet in")

else:
   print (f" Beste {naam}, je bent 18 of ouder en mag dus alleen autorijden met rijbewijs althans")