from funciones import *
import random

Random=palabras('texto_a_leer.txt')
Texto=open('texto_generado.txt','w')
palabra_inicial=Random[randrange(len(Random))]
write(palabra_inicial)
h=histograma('texto_a_leer.txt')
tran=transicion('texto_a_leer.txt',h)
palabra_actual=palabra_inicial
while True:
	a=palabra_despues_otra_posibilidad('texto_a_leer.txt',palabra_actual)
	b=dict()
	tot=0
	for i in a.values():
		tot+=i
	
