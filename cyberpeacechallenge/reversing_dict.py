
dict1 = []
dict1.append({"1":"4","4":"87","9":"c","t":"0f","z":"1","E":"5b","M":"eb","Z":"3"}) 
dict1.append({"3":"45","5":"37","6":"a","c":"a9","h":"1","s":"00","E":"b","K":"c1","L":"3"})
dict1.append({"1":"1","3":"f8","c":"3","f":"6","B":"e0","I":"cc","S":"20","T":"94"})

print(dict1[0].keys())

pass1 = "3a33364bf8"

password = ""

it = iter(range(len(pass1)))

j =0

for i in it:
    
    print(i,j)
    try:
        print(i%3)
        print(list(my_dict.keys())[list(my_dict.values()).index(pass1[i])])
        print("val : ", str(pass1[i]) , "pass : ", dict1[i%3].keys()[list(dict1[i%3].values()).index(str(pass1[i]))] )
        password += dict1[j%3].keys()[list(dict1[j%3].values()).index(pass1[i])]
    except Exception as e:
        print(i%3)
        print("val : ", str(pass1[i]) + str(pass1[i+1]), "pass : ", dict1[i%3].keys()[list(dict1[i%3].values()).index(str(pass1[i]) + str(pass1[i+1]))] )
        password += dict1[j%3].keys()[list(dict1[j%3].values()).index(str(pass1[i]) + str(pass1[i+1]))]
        next(it)
       
    print(password)
    j=j+1
print(password)

# pass2 = "8700e00fa994eb45205b37"

# it = iter(range(len(pass2)))

# for i in it:
    
#     print(i)
#     print("val : ", str(pass2[i]) + str(pass2[i+1]), "pass : ", dict1[i%3].keys()[dict1[i%3].values().index(str(pass2[i]) + str(pass2[i+1]))] )
#     password += dict1[i%3].keys()[dict1[i%3].values().index(str(pass2[i]) + str(pass2[i+1]))]
#     next(it)
       
#     print(password)



#Z6cZLf1E34s
#Z6cZLf1E34sBtcTM3SE5