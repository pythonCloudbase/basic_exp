
file1 = open("cipherText.txt") 

fullList = []

# print(file1.readlines())

outputstr = ""
for i in file1.readlines():
    for j in i:
        # em = (ord(j[-3:])%128000)%128
        em = ord(j[-3:])
        print(em, " : " , hex(ord(j)), " : ", chr(em), " : ", type(j)) 
        #em+=64
        outputstr += chr(em)
        fullList.append(em)
#fullList.sort()
print(outputstr)

#print("max", max(fullList))
#print("min", min(fullList))