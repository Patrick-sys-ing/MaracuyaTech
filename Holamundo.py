
"""
Registrarse en una universidad. Realizar
un programa que le pida al usuario que ingrese 
su edad, si es menor que 18 o mayor que
80 imprimir que no puede registrarse
caso contrado si puede

"""

print ("Bienvenido a la  Universidad MaracuyaTech, ya le ayudo con su inscripcion")
name = input("Me ayuda con su nombre para poder continuar: " )
edad = int(input("Me ayuda con su edad {} para continuar con la inscripcion: ".format(name)))

if not edad<18 and not edad >=80:
	print ("Listo mi estimado podemos proceder con su inscripcion")
	asd = (input("Usted vive aqui?,,, bueno bueno eso da igual *teclea*"))
	print ("Listo {} usted se encuentra registrado en MaracuyaTech".format(name))
else:
	print ("Disculpe, usted no esta en el rango de edad para esta prestigiosa universidad")
	


salir = input("Puedes salir del registro {} presionando cualquier tecla:".format(name))



