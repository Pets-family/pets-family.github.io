liste1 = ["gdklnnfqlp", "fapeakodng", "bniujfkg", "fidoxmropz", "hgifudkml", "jgiofdkngp"]
liste2 = ["cndiogfnle", "fapeakzdng", "bnigjkfg", "mjiogndfea", "hgifuckml", "jgiofdkngp"]
liste3 = [ ]
for i in range(6):
    print(liste1[i] > liste2 [i])
    liste3.append (liste1[i] > liste2 [i])
    print (liste3)
nombre_binaire = ("")
for i in range ( len (liste3)):
    if liste3[i]== True:
        nombre_binaire = nombre_binaire + '1'
    else:
        nombre_binaire =nombre_binaire + '0'
print (nombre_binaire) 
nombre_décimal = int(nombre_binaire, 2)
print (nombre_décimal)
caractère = chr (nombre_décimal)
print (caractère)