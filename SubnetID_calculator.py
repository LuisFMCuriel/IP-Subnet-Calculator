import re

a = False
while a == False:
    print("Ip address")
    ip = input()
    print("Netmask")
    mask = input()
    cont_mask = 0
    cont_ip = 0
    errors = 0
    for l in mask:
        if l == ".":
            cont_mask = cont_mask + 1
    for l in ip:
        if l == ".":
            cont_ip = cont_ip + 1
    if cont_mask == 3 and cont_ip == 3 and len(mask) >= 7 and len(ip) >= 7:
        break
    else:
        print("Wrong input format")

new_ip = ip.replace(".", "_")
new_mask = mask.replace(".", "_")
numbers = [0,0,0,len(new_mask)]
numbers2 = [0,0,0,len(new_ip)]
cont = 0
b = [0,0,0,0]
ID = ""
Br = ""

for k in re.finditer("_", new_mask):
    numbers[cont] = k.start()
    cont = cont + 1

cont = 0

for k in re.finditer("_", new_ip):
    numbers2[cont] = k.start()
    cont = cont + 1  
    
for i in range(0,4):
    if i == 0:
        if int(new_mask[:numbers[0]]) == 0:
            b[i] = 0
            ID = ID + "0."
            Br = Br + "255."
        elif int(new_mask[:numbers[0]]) == 255:
            b[i] = 1
            ID = ID + new_ip[:numbers2[0]] + "."
            Br = Br + new_ip[:numbers2[0]] + "."
        else:
            b[i] = 2
            M = 256 - int(new_mask[:numbers[0]])
            if M > int(new_ip[:number2[0]]):
                ID = ID + "0."
                Br = Br + str(0+M-1) + "."
            else:
                j = 1
                R = 0
                while R < int(new_ip[:numbers2[0]]):
                    R = M*j
                    j = j + 1
                j = j - 2
                ID = ID + str(M*j) + "."
                Br = Br + str((M*j)+M-1) + "."
            
            
    else:
        if int(new_mask[numbers[i-1]+1:numbers[i]]) == 0:
            b[i] = 0
            ID = ID + "0."
            Br = Br + "255."
        elif int(new_mask[numbers[i-1]+1:numbers[i]]) == 255:
            b[i] = 1
            ID = ID + new_ip[numbers2[i-1]+1:numbers2[i]] + "."
            Br = Br + new_ip[numbers2[i-1]+1:numbers2[i]] + "."
        else:
            
            b[i] = 2
            M = 256 - int(new_mask[numbers[i-1]+1:numbers[i]])
            if M > int(new_ip[numbers2[i-1]+1:numbers2[i]]):
                ID = ID + "0."
                Br = Br + str(0+M-1) + "."
            else:
                j = 1
                R = 0
                while R < int(new_ip[numbers2[i-1]+1:numbers2[i]]):
                    R = M*j
                    j = j + 1
                j = j - 2
                ID = ID + str(M*j) + "."
                
                Br = Br + str((M*j)+M-1) + "."
            
new_ID = ID[:len(ID)-1]
new_Br = Br[:len(Br)-1]
print("Subnet ID: " + new_ID)
print("Broadcast Address: " + new_Br)