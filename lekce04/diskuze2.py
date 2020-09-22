pocetAlena = 4
pocetPetr = pocetAlena * 2
pocetPavla = (pocetAlena + pocetPetr) * 5

print("Počet příspěkvů Aleny: ", pocetAlena, ".")
print("Počet příspěvků Petra: ", pocetPetr, ".")
print("Počet příspěvků Pavly: ", pocetPavla, ".")

if pocetPavla == 1:
    print("Pavla by musela napsat", pocetPavla, "příspěvěk.")

if pocetPavla > 1 and pocetPavla < 5:
    print("Pavla by musela napsat", pocetPavla, "příspěvky.")

else:
    print("Pavla by musela napsat", pocetPavla, "příspěvků.")