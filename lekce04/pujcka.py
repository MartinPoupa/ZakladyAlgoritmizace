P = 10000
r = 8 / 100
n = 12
t = 1

A = round(P * (1 + r / n) **(n * t))

print("Půjčil/a jsem si", P, "korun s úrokem", r, "p.a.")

if t <= 1:
    print("Budu je splácet", n, "krát ročně po dobu", t, "roku.")
else:
    print("Budu je splácet", n, "krát ročně po dobu", t, "let.")

print("Dohromady vrátím", A, "korun.")