L = [2,4,7,11]
LCopy = L.copy()
Order = []
maxIndex = []
maxDiff = -1000

for i in range(len(L)):
  for j in range(len(L)):
    a = abs(L[i]-L[j])
    if maxDiff < a:
      maxIndex.clear()
      maxDiff = a
      maxIndex.append(i)
      maxIndex.append(j)

Order.append(L[maxIndex[0]])
Order.append(L[maxIndex[1]])
LCopy.remove(L[maxIndex[0]])
LCopy.remove(L[maxIndex[1]])
maxDiff = -1000
maxIndex.clear()

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