import os
import sys

#Variables:
cont=1

#lista de listas de tuplas, como dice el nombre, es una lista que almacena tuplas en orden

libros=[ 
 ("0","IT","Stephen King","Recreativo","Novela","Terror","Cuenta la historia de un grupo de siete niños que son aterrorizados por un malvado monstruo -al que llaman «Eso»- que es capaz de cambiar de forma, alimentándose del terror que produce en sus víctimas."),
 ("1","El Señor de los Anillos","J.R.R Tolkien","Recreativo","Novela","Fantasia Epica","Su historia se desarrolla en la Tercera Edad del Sol de la Tierra Media, un lugar ficticio poblado por hombres y otras razas antropomorfas como los hobbits, los elfos o los enanos, así como por muchas otras criaturas reales y fantásticas. La novela narra el viaje del protagonista principal, Frodo Bolsón, hobbit de la Comarca, para destruir el Anillo Único y la consiguiente guerra que provocará el enemigo para recuperarlo, ya que es la principal fuente de poder de su creador, el Señor oscuro Sauron."),
 ]

 #Podi diferenciar una lista y una tupla viendo con que corchete empieza, si empieza con un "()" es una tupla, si empieza con un "[]" es una lista

def ext():    #Funcion que cada vez que es llamada imprime una linea vacia y llama al menu
 print("\n")   
 print(menu()) #llama a la funcion menu()
 
def agr():  #Esta funcion es para agregar informacion a la lista "libros" 
  temp=[]    #Defino una variable temporal que se usara para agregar informacion
  global cont #Se define como global una variable para "Stackear" su valor y no perderlo
  cont=cont+1
  temp.append(cont)  #Con esto se agrega la ID a cada libro, la cual aumenta en 1 cada vez que se agrega uno
  tit=str(input("\nIngrese el titulo del libro: "))
  temp.append(tit)
  aut=str(input("Ingrese el autor del libro: "))
  temp.append(aut)
  tip=str(input("Ingrese el tipo del libro: "))      #en esta seccion basicamente pido datos, y los meto dentro de la lista temporal llamada "temp" o temporal
  temp.append(tip)
  gen=str(input("Ingrese el genero del libro: "))
  temp.append(gen)
  subgen=str(input("Ingrese el subgenero del libro: "))
  temp.append(subgen)
  desc=str(input("Ingrese la descripcion del libro: "))
  temp.append(desc)
  tuple(temp)  
  libros.append(temp) #agrego a la lista de "libros" la tupla llamada "temp"
  del temp  #formateo temp para poder usarla en otra ocasion
  print(ext()) #llamo a la funcion de salida que invoca un menu

def mov():
 print("Para ""mover"" un libro dentro del sistema, debe hacerse con su ID")   
 ido=int(input("\nIngrese el ID del libro a mover: "))
 idc=int(input("Ingrese el ID que quiere asignar: "))
 for ids,titulo,autor,tipo,genero,subgenero,descripcion in libros:
  libros.remove(ido)
  libros.insert(0, idc)  
 print("La ID de:",titulo,"Ha sido cambiada por:",idc)
 print(ext())
 
    

def remov(): #funcion que sirve para remover un libro o limpiar el "catalogo" entero
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
   libros.pop(idb)
   print("El libro con el ID:",idb,"y titulo:",titulo,"ha sido borrado del catalogo")
   print("Volviendo al menu principal")
   print(ext())
  else:
   idb=int(input("¿Que libro desea eliminar?(Ingrese la ID del libro):" ))
   libros.pop(idb) #llamo a la funcion pop que elimine al libro con esa id(la cual es asignada segun posicion en la lista)
   print("El libro con el ID:",idb,"y titulo:",titulo,"ha sido borrado del catalogo")
   print("Volviendo al menu principal")
   print(ext())
   
 else:
  libros.clear()
  print("Todos los libros del catalogo han sido borrados")
 print(menu())

def most(): #esta funcion sirve para desempaquetar las tuplas contenidas en la lista "libros" 
            #y muestra su contenido de manera ordenanda
 if libros:  #Si existen elementos en la lista, se hace esto:
  for ids,titulo,autor,tipo,genero,subgenero,descripcion in libros:
   print("\n########################################################################")   
   print("ID:",ids,"\nTitulo:",titulo,"\nAutor:",autor,"\nTipo:",tipo,"\nGenero-Subgenero:",genero,"-",subgenero,"\nDescripcion:",descripcion)
 else: #Si no existen elementos manda ese print y vuelve al menu
  print("\nNo hay nada en el catalogo")   
 print(ext())
 
def menu(): #simplemente una funcion que sirve de menu en el programa
 print("\t Biblioteca Virtual")
 print("\nMenu de opciones:")   
 print("[1] Agregar libro al registro")
 print("[2] Eliminar libros del registro")
 print("[3] Mover libros en el registro (No supe hacer que funcionara bien)")
 print("[4] Mostrar libros en el registro")
 print("[5] Para limpiar la pantalla")
 print("[6] Salir del programa")
 opc=int(input("\nIngrese la opcion:"))
 
 if opc==1:
  print(agr())
 if opc==2:
  print(remov())   
 if opc==3:
  print(mov())   
 if opc==4:
  print(most())
 if opc==5:
  os.system("cls")   #limpio la pantalla con ayuda del modulo system y llamo la funcion
  print(ext())       #de salida que muestra otra ves el menu
 if opc==6:   
  sys.exit()          #funcion del modulo "sys" que permite salirse del programa sin errores y weas raras
  
print(menu())

#marcas de agua por si las moscas maldito qlo



