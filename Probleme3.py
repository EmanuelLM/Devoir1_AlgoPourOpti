L = [3,5,8,9]
diff = []
alert = 0 
for i in range(len(L)):
  for j in range(len(L)): 
    diff.append(abs(L[i]-L[j]))

for i in range(len(diff)):
  x = 0
  checking = diff[i]
  for j in range(len(diff)) :
    if checking == diff[j] and checking != 0 :
      x = x+1
      if x > 2 :
        alert = 1 
      
if alert == 1 :
  print("interference detected")

diff.sort()
print(diff)
