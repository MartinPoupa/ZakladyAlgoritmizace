sirka = 45
delka = 70
pocetKol = 20
print("Šířka hřiště je", sirka, "metrů, délka je", delka, "metrů.")
print("Jedno kolo okolo hřiště je", 2 * (delka + sirka), "metrů.")

if pocetKol <= 1:
    print("Po", pocetKol, "kole uběhneš", (sirka + delka) * pocetKol, "metrů.")

else:
    print("Po", pocetKol, "kolech uběhneš", (sirka + delka) * pocetKol, "metrů.")