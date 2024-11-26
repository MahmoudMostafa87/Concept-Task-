liste=[]
while True:
    condition=int(input("if you want add steps enter 1 if not enter anything"))
    if(condition==1):
        while True:
            steps=int(input("enter steps"))
            if(steps.is_integer()):liste.append(steps)
            else :break
    else:
        break
maxe=0
mine=0
for x in liste:
    if(mine>x):mine=x
    if(maxe<x):maxe=x
print(f"max = {maxe} min = {mine}")
print(round(sum(liste)/len(liste)))
liste.sort(reverse=True)
print(liste)

























