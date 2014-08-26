from funciones import *
from random import *

Random=palabras('texto_a_leer.txt')
Texto=open('texto_generado.txt','w')
palabra_inicial='Los'
Texto.write(palabra_inicial+' ')
palabra_actual=palabra_inicial
cont=0
while True:
	a=palabra_despues_otra_posibilidades('texto_a_leer.txt',palabra_actual)
	b=list()
	for i in a:
		for x in range(a[i]):
			b.append(i)
	palabra_actual=choice(b)
	Texto.write(palabra_actual)
	Texto.write(' ')
	cont+=1
	if cont==50:
		break
Texto.close()
