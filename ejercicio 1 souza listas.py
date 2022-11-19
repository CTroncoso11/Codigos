cnt=1
num=[]
sump=0

while cnt<=10: 
 print("LLevas:",cnt,"de 10")
 nume=int(input("Ingrese un numero: "))
 
 num.append(nume)
 cnt+=1

for numeros in num:
 sump=sump+numeros

promf=sump/10
men=min(num)
may=max(num)


print("\nLa suma total es:",sump)
print("El promedio final es:",promf)
print("El numero menor es:",men)
print("El numero mayor es:",may)

 
