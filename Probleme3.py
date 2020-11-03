L = [3,5,8,9] #Liste de canaux sélectionnés
diff = [] #Liste contenant les différence entre les paires contenues dans L
alert = 0 #Variable binaire nous signalant si il y a risque d'interférence 
for i in range(len(L)):
  for j in range(len(L)): 
    diff.append(abs(L[i]-L[j]))

for i in range(len(diff)):
  x = 0
  checking = diff[i]
  for j in range(len(diff)) :
    if checking == diff[j] and checking != 0 : #On va calculer la différence entre tous les nombres donc il ne faut pas compter les différence nulles 
      x = x+1
      if x > 2 : #Comme la valeur absolue est la même pour une paire, la contrainte sera violée quand on dépassera le doublon dans diff[] (plus de 2 différences identiques)
        alert = 1 
      
if alert == 1 :
  print("interference detected")

diff.sort()
print(diff)
