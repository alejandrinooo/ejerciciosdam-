import re  

#1
frase="hola juan perez tu balance es"
moneda="$"
cantidad=53.44

print ("%s %f %s" % (frase,cantidad, moneda))

#2

a_float = float("3.14")
cadena = str(a_float)
print(type(a_float))
print(type(cadena))

#3
numero=2
cadena="hola mundo"
len(cadena)
decimal=7.5


#4
cadenatrim ='   abc   '
print(cadenatrim.rstrip())

cadenasplit = "hola, soy, alejandro"
cadenasplit.split(",")

string = "ESTO SON MAYUSCULAS"
print(string.lower())

string = "esto son minusculas"
print(string.capitalize())

linea = ('soy alejandro.')
letra = linea.find('o')
print(letra)

vocales = ['a', 'e', 'i', 'o', 'i', 'u']
index = vocales.index('e')

txt = "Hola mundo"
x = txt.startswith("Hola")
print(x)

#5
primerafrase="En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor"
buscar=re.findall(r'a',primerafrase)
print(len(buscar))