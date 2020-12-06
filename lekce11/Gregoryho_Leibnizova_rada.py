a = 10**7
sum = 0
for i in range(0, a):
    sum = sum + ((-1) ** i) / (2 * i + 1)
sum = 4 * sum 
print(sum)
