def gen_mat_igual():
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
 print("######################################################\n") 
 print(mat)
 print("######################################################\n")
 menu()
 
def gen_mat_dif():
 mat=[]
 temp=[]
 limit=0
 global cont1
 cont1=0
 cont2=0
 ancho=int(input("Ingrese el ancho: "))
 largo=int(input("Ingrese el largo: "))


 while cont2<=largo:
  while cont1<=ancho:
   temp.append(cont1)
   cont1=cont1+1
  mat.append(temp)
  cont2+=1
 print("######################################################\n") 
 print(mat)
 print("######################################################\n")
 menu()
def menu():
  print("[1] Para generar una matriz con valor igual por fila")
  print("[2] Para generar una matriz con valor diferente por fila")
  opc=int(input("Ingrese la alternativa: "))
  if opc==1:
   gen_mat_igual()
  if opc==2:
   gen_mat_dif()

menu()   
    
