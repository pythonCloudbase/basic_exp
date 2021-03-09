file1 = open("cipherText.txt", encoding='utf-8') 

fullList = []

print(file1.readlines())

for i in file1.readlines():
    for j in i:
        #print(ord(j))
        fullList.append(ord(j))

# print(chr(128))

# for i in fullList:
#     # new = int(i%128000 -480)
#     if(new >0):
#         print(new, " - ", chr(new))


#print(uniqueList)
#print(len(uniqueList))
uniqueList = list(set(fullList))

print(128587 in uniqueList)

print(uniqueList, len(uniqueList))

uniqueList.remove(10)
#fullList.remove(10)

# print('here: ', 128587 in uniqueList)

#print(uniqueList, len(uniqueList))

#uniqueCharlist = [chr(x) for x in range(65, 119)]
uniqueCharlist = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz."
#uniqueCharlist = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=}[]:\"';<>?/,{"

print(len(uniqueCharlist), len(uniqueList))

dictEmoji = {}

for i, element in zip(uniqueCharlist, uniqueList):
    print(i, " : ", chr(element))
    dictEmoji[element]  = i

dictHex = {}

for i in uniqueList:
    print(i, " : ", hex(i))
    dictHex[i]  = hex(i)


# handling \n
dictEmoji[10] = '\n'

print(fullList)


convertedText = ""

#print(128587 in dictEmoji.keys())

#print(128587 in fullList)



for i in fullList:
    convertedText += dictEmoji[i]
 
print(convertedText)