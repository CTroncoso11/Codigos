"""
11. El jerigonzo es una variante ludica del habla en las que se intercalan silabas 
entre medio de una palabra en forma reiterada. 
Para traducir una oracion a jerigonzo despues de cada vocal se debe agregar el 
sonido \p" y luego repetir la vocal. Por ejemplo si tenemos la oracion hola mundo, 
entonces traducido al jerigonzo seria: hopolapa mupundopo. 
Desarrolle un algoritmo que traduzca alguna oracion a jerigonzo.
"""
print ("\n\t Desarrollo  Jerigonzo ")

cadena=""
largo=0
i=0
aux = " "
cadena= input("\n\tIngrese cadena (solo minisculas) :")
print ("\tCadena ingresada  :", cadena)
largo=len(cadena)
print ("\n\t  Largo de la Cadena  :", largo)

while i<=largo-1:
    if (cadena[i]!="a" and  cadena[i]!="e") and  (cadena[i]!="i" and  cadena[i]!="o") and  cadena[i]!="u":
        aux = aux + cadena[i]
    elif  cadena[i] =="a":
        aux =aux + "apa"
    elif  cadena[i] =="e":
        aux =aux + "epe"
    elif  cadena[i] =="i":
        aux =aux + "ipi"
    elif  cadena[i] =="o":
        aux =aux + "opo"
    else:
        aux =aux + "upu"
    i=i+1

print ("\n\t  Cadena nueva: ", aux)
        
