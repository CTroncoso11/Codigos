import os

#Variables:

#lista de listas de tuplas
libros=[  
("1","IT","Stephen King","Recreativo","Novela","Terror","Cuenta la historia de un grupo de siete niños que son aterrorizados por un malvado monstruo -al que llaman «Eso»- que es capaz de cambiar de forma, alimentándose del terror que produce en sus víctimas."),
]

def ext():
 print("\n")   
 print(menu())
 
def agr():
  temp=[]   
  cont=2   
  temp.append(cont)
  cont+=1
  tit=str(input("\nIngrese el titulo del libro: "))
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
  print(ext())

def remov():
 print("\n¿Que desea hacer?")
 print("[1] Para borrar un libro especifico")
 print("[2] Para borrar todo el catalogo")
 alt=int(input("Ingrese la opcion seleccionada:"))
 
 if alt==1:
  print("¿Desea ver la lista actual de libros?")
  alte=int(input("Ingrese la opcion([1]Si [2]No): "))

  if alte==1:
   for ids,titulo,autor,tipo,genero,subgenero,descripcion in libros:
    print("########################################################################")   
    print("ID:",ids,"\nTitulo:",titulo,"\nAutor:",autor,"\nTipo:",tipo,"\nGenero-Subgenero:",genero,"-",subgenero,"\nDescripcion:",descripcion)
   idb=int(input("\n ¿Que libro desea eliminar?(Ingrese la ID del libro):" ))
   print("\nSe ha borrado la siguiente informacion del catalogo: ")
   libros.pop(idb)
   print("El libro con el ID:",idb,"ha sido borrado del catalogo")
   print("Volviendo al menu principal")
   print(ext())
  else:
   idb=int(input("¿Que libro desea eliminar?(Ingrese la ID del libro):" ))
   az=idb
   libros.remove(az)
   
 else:
  libros.clear()
  print("Todos los libros del catalogo han sido borrados")
 print(menu())

def most():
 for ids,titulo,autor,tipo,genero,subgenero,descripcion in libros:
  print("########################################################################")   
  print("ID:",ids,"\nTitulo:",titulo,"\nAutor:",autor,"\nTipo:",tipo,"\nGenero-Subgenero:",genero,"-",subgenero,"\nDescripcion:",descripcion)
 print(ext())
 
def menu():
 print("Menu de opciones:")   
 print("[1] Agregar libro al registro")
 print("[2] Eliminar libros del registro")
 print("[3] Mover libros en el registro")
 print("[4] Mostrar libros en el registro")
 print("[5] Para limpiar la pantalla")
 print("[6] Salir del programa")
 opc=int(input("\n Ingrese la opcion:"))

 if opc==1:
  print(agr())
 if opc==2:
  print(remov())   
 if opc==3:
  print("En desarrollo")   
 if opc==4:
  print(most())
 if opc==5:
  os.system("cls")
  print(ext())  
 if opc==6:
  print("En desarrollo")   



print("\t Biblioteca Virtual")
print(menu())



