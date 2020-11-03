a1 = 2
b1 = 3
a2 = 5
b2 = 1
x = 4

def algoSecant (a1,b1,a2,b2,x) :
  y1 = a1*x+b1
  print("y1",y1) #Coordonnée y1 apd a1+b1 et x fixé 
  y2 = a2*x+b2
  print("y2",y2) #Coordonnée y1 apd a1+b1 et x fixé 
  while abs(y1-y2) > 0.00000000001: #Tant que ces coordonnées sont différentes 
    y = (y1+y2)/2 #Prendre la moyenne des 2 coord. en y 
    x1 = (y-b1)/a1 #Récupérer le x1 correspondant à l'y moyen 
    x2 = (y-b2)/a2 #Récupérer le x2 correspondant à l'y moyen 
    x = (x1+x2)/2 #Prendre la moyenne des 2 coord. en x 
    y1 = a1*x + b1 #Réinjecter nouveau x pour avoir nouveaux y moyen
    y2 = a2*x + b2 #Réinjecter nouveau x pour avoir nouveaux y moyen
  y= (y1+y2)/2 #Prendre la moyenne pour trouver nouveau y
  return x,y

print(algoSecant (a1,b1,a2,b2,x)) #Trouve le point d'intersection entre deux 
#droite d'intersection spécifié dans les paramètres 
