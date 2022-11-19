mat=[]
temp=[]
limit=0
global cont1
cont1=1
cont2=0
ancho=int(input("Ingrese el ancho: "))
largo=int(input("Ingrese el largo: "))


while cont2<=largo:
 while cont1<=ancho:
  temp.append(cont1)
  cont1=cont1+1
 mat.append(temp)
 cont2+=1
print(mat)
