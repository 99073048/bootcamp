
# Opdracht 4.

# Joris de Tester heeft een programma geschreven om de kosten van vloerbedekking te berekenen. Er zijn staffelprijzen (afwijkende prijzen voor grote bestellingen) voor verschillende hoeveelheden. 
# Er zit echter een fout in de code die moet worden verbeterd. Kun jij helpen? 😊

oppervlakte = int(input('Hoeveel m2 vloerbedekking heeft u nodig?'))

prijs_m2 = 40
if  oppervlakte >= 150:
  prijs_m2 = 35
elif oppervlakte >= 80: 
  prijs_m2 = 38

totaal = prijs_m2 * oppervlakte

print(f'Het totaalbedrag is voor een oppervlakte van {oppervlakte} m2 is: Eur ' + str(totaal))

# een elif is eigelijk een alternatief voor else 
#Het gebruik van str(totaal) in de printverklaring is nodig omdat totaal een numerieke waarde is (het berekende totaalbedrag), en de print-functie verwacht een string als argument om af te drukken. Door str(totaal) te gebruiken, wordt de numerieke waarde van totaal omgezet in een string, zodat deze correct kan worden samengevoegd met de rest van de tekst in de uitvoerzin.