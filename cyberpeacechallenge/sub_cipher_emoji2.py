file1 = open("cipherText.txt")

fullList = []


for i in file1.readlines():
    for j in i:
        #print(ord(j))
        try:
            fullList.append(hex(ord(j)))
        except Exception as e:
            print(e)

for i in fullList:
    try:
        print((hex(i[-2:])))
    except Exception as e:
        print(e)

# print(chr(128))

# for i in fullList:
#     # new = int(i%128000 -480)
#     if(new >0):
#         print(new, " - ", chr(new))


#print(uniqueList)
#print(len(uniqueList))
# uniqueList = list(set(fullList))

# print(128587 in uniqueList)

# print(uniqueList, len(uniqueList))

# uniqueList.remove(10)
# #fullList.remove(10)

# # print('here: ', 128587 in uniqueList)

# #print(uniqueList, len(uniqueList))

# #uniqueCharlist = [chr(x) for x in range(65, 119)]
# uniqueCharlist = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz."
# #uniqueCharlist = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=}[]:\"';<>?/,{"

# print(len(uniqueCharlist), len(uniqueList))

# dictEmoji = {}

# codeword = [':rocket:', ' :steam_locomotive:', ':smiley:', ' :smile:', ' :sweat_smile:', ' :innocent:', ' :light_rail:', '']
# codeword  = ['r', 's', ]


# for i, element in zip(uniqueCharlist, uniqueList):
#     print(i, " : ", chr(element))
#     dictEmoji[element]  = i

# # handling \n
# dictEmoji[10] = '\n'

# print(fullList)


# convertedText = ""

# #print(128587 in dictEmoji.keys())

# #print(128587 in fullList)



# for i in fullList:
#     convertedText += dictEmoji[i]
 
# print(convertedText)