
#Ejercicio  01
#Imprimir los números entre el 5 y el 20, saltando de tres en tres
for i in range(5,20,3):
  print(i)



#Ejercicio 02:
#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
import pyautogui
#solicita una palabra al usuario
palabra = pyautogui.prompt(text="Ingrese una palabra", title="Solicitud", default="")
for i in range(10):
  print(palabra)


# Ejercicio 03:
# Escriba un programa que valide si el dato ingresado por el usuario 
# corresponde a un correo electrónico, para ello debe comprobar  
# si existe o no el carácter @ en el dato ingresado por el usuario.
import pyautogui
#solicita una palabra al usuario
email = pyautogui.prompt(text="Ingrese su email", title="Solicitud", default="ingrese aquí su email")
condicion = False
#Blucle
for i in email:
  if (i == "@"):
    condicion = True

if (condicion==True):
  print("Dato ingresado sí es un email")
else:
  print("Dato ingresado no es un email")





 