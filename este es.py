from funciones import *
import random

Random=palabras('texto_a_leer.txt')
Texto=open('texto_generado.txt','w')
palabra_inicial=Random[randrange(len(Random))]
write(palabra_inicial)
h=histograma('texto_a_leer.txt')
tran=transicion('texto_a_leer.txt',h)
palabra_actual=palabra_inicial
cont=0
while True:
	a=palabra_despues_otra_posibilidad('texto_a_leer.txt',palabra_actual)
	b=list()
	for i in a:
		for x in range(a[i]):
			b.append(i)
	palabra_actual=choice(b)
	Texto.write(palabra_actual)
	cont+=1
	if cont==50:
		break
Texto.close()