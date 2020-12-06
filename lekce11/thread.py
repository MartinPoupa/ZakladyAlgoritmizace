import threading
a = 1000
b = 10**6

threads = [None] * a
results = [None] * a

def caucalition(c, d, index):
    global results
    sum = 0
    for i in range(c, d):
        sum = sum + ((-1) ** i) / (2 * i + 1)
    results[index] = sum

for i in range(a):
    threads[i] = threading.Thread(target=caucalition, args=(b*i, b*(i+1), i,))

for i in range(a):
    threads[i].start()
    print(i)
    
f = True
while f:
    g = False
    e = 0
    for i in range(a): 
        g = g or threads[i].is_alive()
        if threads[i].is_alive():
            e = e + 1
    print(e)
    f = g
    
pi = 0
for i in range(a):
    if results[i] is not None :
        pi = pi + results[i]
pi = pi * 4
print (pi)
