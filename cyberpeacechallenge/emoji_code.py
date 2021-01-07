import emoji

file1 = open("cipherText.txt", encoding='utf-8') 

fullList = []

# print(file1.readlines())

for i in file1.readlines():
    for j in i:
        print(hex(ord(j)))
        fullList.append(hex(ord((j))))
fullList.sort()
print(fullList)

print("max", max(fullList))
print("min", min(fullList))

freqList ={}

for i in fullList:
    if(!f[i]0)


# print()
# print(emoji.demojize("😯"))