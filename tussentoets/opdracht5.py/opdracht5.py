# # opdracht 5
# Opdracht 5.

# Joris de Tester heeft het probleem opgelost. Helaas heeft hij wel weer een volgende uitdaging: 
# Gevraagd is tussen input en print 3 keer te printen: 
# "Een moment geduld a.u.b., de scherpste prijs wordt berekend."
# Voor het effect wacht het programma steeds een seconde.

# Joris is aan de slag gegaan en heeft de volgende code opgeleverd:

 # je hoeft nog niet te weten wat een import is, Kopieer deze regel en je kunt je programma laten wachten met de opdracht sleep(x seconden)

from time import sleep

oppervlakte = int(input('Hoeveel m2 vloerbedekking heeft u nodig?'))
prijs_m2 = 40

# hier moet een delay
print("Een moment geduld a.u.b., de scherpste prijs wordt berekend.")
sleep(1)

totaal = prijs_m2 * oppervlakte

print(f'Het scherpste prijs voor een oppervlakte van {oppervlakte} m2 is: Eur ' + str(totaal))

# constante berekeneing voor aantal meldingen die komen

aantal_meldingen= 5

