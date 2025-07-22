slovo = input("Введите слово латиницей: ")

a = 0
e = 0
i = 0
o = 0
u = 0

ind = 1

for ind in range(len(slovo)):
    b = slovo[ind]
    if b == 'a':
        a = a + 1
    elif b == 'e':
        e = e + 1
    elif b == 'i':
        i = i + 1
    elif b == 'o':
        o = o + 1
    elif b == 'u':
        u = u + 1

    ind += 1

gl = a + e + i + o + u

sogl = len(slovo) - gl

print("Гласных:", gl)
print("Согласных:", sogl)

if a!=0: print("Букв a:", a)
else: print("Букв a нет")
if e!=0: print("Букв e:", e)
else: print("Букв e нет")
if i!=0: print("Букв i:", i)
else: print("Букв i нет")
if o!=0: print("Букв o:", o)
else: print("Букв o нет")
if u!=0: print("Букв u:", u)
else: print("Букв u нет")