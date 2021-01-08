f1 =  open('wl1.txt')
f2 = open('wl2.txt')

wordlist = []
f1_words = f1.readlines()
f2_words = f2.readlines()

for z in range(100):
    for i in f1_words:
        for j in f2_words:
            wordlist.append(i.strip()+j.strip()+ str(z).zfill(2))

print("\n".join(wordlist))