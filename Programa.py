import sys, os
opc=0
def agregar_cuota():
 print("sss")

def menu():
 print("[1] Ingresar cuota")
 print("[2] Consultar cuotas por RUT")
 print("[3] Consultar deudas por RUT")
 print("[4] Salir del progrma")
 opc=int(input("Ingrese una opcion: "))
 if opc==1:
  agregar_cuota()
 if opc==2:
  consultar_cuotas()
 if opc==3:
  consultar_deuda()
 if opc==4:
  sys.exit()
        
menu()                                       
