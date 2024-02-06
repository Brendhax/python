j = input("Você está em jejum s/n? ")
t = input("Trigliceres? ")
t = int(t) # converter pra int 
if j == 's':
    if t > 150:
        print ("Esrtá alto !")
    else:
        print("Está normal !")
else:
    if t > 175:
        print ("Esrtá alto !")
    else:
        print("Está normal !")