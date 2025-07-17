volcanes = ["Villarrica", "Osorno", "Llaima", "Lonquimay", "Calbuco", "Puntiagudo", "Descabezado Grande", "Nevados de Chillán"]

for i in range(len(volcanes)):
  print (volcanes[i])

for i,v in enumerate(volcanes):
   print(i,v)




#para imprimir los que empiezan con P

for i, v in enumerate(volcanes):
   if v[0] == "P":
        print(i , v)

#para iterar con while

i = 0
while i < len(volcanes):
    print(volcanes[i])
    i += 1 

#ordenar alfabeticamente
print(sorted(volcanes))

#ordenar alfabeticamente mas largo
volcanes.sort()
print(volcanes)