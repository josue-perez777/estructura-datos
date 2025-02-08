temperatura=[]
for n in range (0,5):
t= int(input("ingrese la temperatura"))
temperatura.append(t)

promedio= sum (temperatura)/len(temperatura)

print("la temperatura promedio es :",promedio)
if promedio < 20:
    print ("nesecita una revision")
elif 20 >= promedio <= 30:
    print("la temperatura esta bien")
else:
    print("se necesita una revision de los conductos del aire")
    