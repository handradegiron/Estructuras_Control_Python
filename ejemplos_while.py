# Ejercicio 1:
# Escriba un programa que solicite un número al usuario; el programa 
# debe seguir solicitando dicho número, mientras que el dato 
# ingresado por el usuario sea menor de 10. 

numero = int(input("Ingrese un número: "))
while numero<10:
    numero = int(input("Ingrese un número"))   
print (numero)


# Ejercicio 2.1:
# Escriba un programa que solicite al usuario el ingreso de su contraseña, 
# el programa debe seguir solicitando la contraseña mientras lo ingresado 
# no coincida con la clave correcta. 

clave="123456"
condicion = True
while condicion==True:
	password = input("Ingrese clave: ")
	if(clave==password):
		print("Clave correcta")
		condicion = False



#Ejercicio 2.2:
#Escriba un programa que solicite al usuario el ingreso de su contraseña,
#debe solicitarse haciendo uso de interface gráfica de usuario. 
#El programa debe seguir solicitando la contraseña mientras lo ingresado 
#no coincida con la clave correcta. 
import pyautogui
clave="1234"
condicion = True
while condicion:
	password = pyautogui.password(text='Ingrese su contraseña', title='Ingrese datos', default='', mask='*')
	if(clave==password):
		pyautogui.alert(text='LA CLAVE ES CORRECTA', title='Mensaje', button='OK')		
		condicion = False
	else:
		pyautogui.alert(text='LA CLAVE ES INCORRECTA', title='Mensaje', button='OK')		
		


#Prorama de adivinanza de números
import random
num_aleatorio = random.randint(0,100)
condicion = True
contador = 1
while(condicion):
	numero= input("Adivine el número entre [0-100]: ")
	
	if (num_aleatorio==int(numero)):
		print(f"FELICITACIONES, adivinó el número en {contador} intentos")
		condicion=False
	else:

		if(num_aleatorio<int(numero)):
			print("El número buscado es menor")
			contador = contador + 1
		else:
			print("El número buscado es mayor")
			contador = contador + 1

