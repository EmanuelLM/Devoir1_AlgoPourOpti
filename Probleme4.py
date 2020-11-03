L = [2,4,7,11]
LCopy = L.copy()
Order = []
maxIndex = []
maxDiff = -1000

#Trouver la plus grande différence dans les paires contenues dans L 
for i in range(len(L)):
  for j in range(len(L)):
    a = abs(L[i]-L[j])
    if maxDiff < a:
      maxIndex.clear()
      maxDiff = a
      maxIndex.append(i)
      maxIndex.append(j)
      
#Les rajouter dans notre liste ordonnée et la supprimer de notre liste temporaire 
Order.append(L[maxIndex[0]])
Order.append(L[maxIndex[1]])
LCopy.remove(L[maxIndex[0]])
LCopy.remove(L[maxIndex[1]])
maxDiff = -1000
maxIndex.clear()

#Trouver la plus grande différence entre le dernier nombre dans la liste ordonnée et les nombres restants dans la liste temporaire 
while len(LCopy) != 0:
  for i in range(len(LCopy)) : 
    a = abs(Order[len(Order)-1] - LCopy[i])
    if maxDiff < a :
      maxIndex.clear()
      maxDiff = a
      maxIndex.append(i)
  Order.append(LCopy[maxIndex[0]])
  LCopy.remove(LCopy[maxIndex[0]])


print(Order)
