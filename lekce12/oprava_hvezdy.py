def stars(n):
    const = 5
    for i in range(n):
        print("*", end="")
        if (i + 1)/const == (i + 1)//const:
            print("|", end="")
    print()
stars(7)
stars(15)
stars(255)
