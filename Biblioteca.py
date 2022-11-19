
#Variables:
cont=2

temp=[]


libros=[   #lista de listas de tuplas
("1","IT","Stephen King","Recreativo","Novela","Terror","Cuenta la historia de un grupo de siete niños que son aterrorizados por un malvado monstruo -al que llaman «Eso»- que es capaz de cambiar de forma, alimentándose del terror que produce en sus víctimas."),
]


def menu():
 print("Menu de opciones:")   
 print("[1] Agregar libro al registro")
 print("[2] Eliminar libros del registro")
 print("[3] Mover libros en el registro")
 print("[4] Mostrar libros en el registro")
 opc=int(input("\n Ingrese la opcion:"))
def agr:
    


 if opc==1:
  temp=[]   
  cont=2   
  temp.append(cont)
  cont+=1
  tit=str(input("Ingrese el titulo del libro: "))
  temp.append(tit)
  aut=str(input("Ingrese el autor del libro: "))
  temp.append(aut)
  tip=str(input("Ingrese el tipo del libro: "))
  temp.append(tip)
  gen=str(input("Ingrese el genero del libro: "))
  temp.append(gen)
  subgen=str(input("Ingrese el subgenero del libro: "))
  temp.append(subgen)
  desc=str(input("Ingrese la descripcion del libro: "))
  temp.append(desc)
  tuple(temp)
  libros.append(temp)
  del temp
  for ids,titulo,autor,tipo,genero,subgenero,descripcion in libros:
   print("########################################################################")   
   print("ID:",ids,"\nTitulo:",titulo,"\nAutor:",autor,"\nTipo:",tipo,"\nGenero-Subgenero:",genero,"-",subgenero,"\nDescripcion:",descripcion)
  

 
 if opc==4:
  for ids,titulo,autor,tipo,genero,subgenero,descripcion in libros:
   print("########################################################################")   
   print("ID:",ids,"\nTitulo:",titulo,"\nAutor:",autor,"\nTipo:",tipo,"\nGenero-Subgenero:",genero,"-",subgenero,"\nDescripcion:",descripcion)

print("\t Biblioteca Virtual")
print(menu())



