
#Ejercicio 01:
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla
#si es mayor de edad o no.

import pyautogui
#solicita al usuario su edad
edad = pyautogui.prompt(text="Ingrese su edad", title="Solicitud", default="")
#Convertir a número entero
num_edad = int(edad)
#Evalua condición y segun resultado imprime en pantalla respuesta con print()
if(num_edad>=18):
	print("Usted es mayor de edad")
else:
	print("Usted es menor de edad")



#Ejercicio 02:
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
import pyautogui
#solicita al usuario un número entero
numero = pyautogui.prompt(text="Ingrese un número entero", title="Solicitud", default="")
#Convertir cadena a int
num_int = int(numero)
#Evalua condición y segun resultado imprime en pantalla respuesta con print()
if (num_int % 2 == 0):
 	print("El número " + str(num_int) + " es par")
else:
    print("El número " + str(num_int) + " es impar")

 

#Ejercicio 03
#Para tributar un determinado impuesto se debe ser mayor de 18 años y tener unos ingresos iguales o 
#superiores a 1000 soles mensuales. Escribir un programa que pregunte al usuario su edad y su 
#ingreso mensual y muestre por pantalla si el usuario tiene que tributar o no.

import pyautogui
#solicita al usuario un número entero
edad = pyautogui.prompt(text="Ingrese su edad", title="Solicitud", default="")
ingreso = pyautogui.prompt(text="Registre su ingreso mensual", title="Solicitud", default="")

#Convertir de edad a int
num_edad = int(edad)
#Convertir ingreso a float
num_ingreso = float(ingreso)
#Evalua condición y segun resultado imprime en pantalla respuesta con print()
if (num_edad>=18  and num_ingreso>1000):	
 	print("Paga impuesto")
else:
	print("No paga impuesto")

	     