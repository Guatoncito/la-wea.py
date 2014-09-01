#Benjamin Menses 201473007-1
#Sebastien Sanhueza 201473089-6
#Jose Tello 201473086-
from funciones import *
from random import *

Random=palabras('texto_a_leer.txt')
Texto=open('texto_generado.txt','w')
palabra_inicial=Random[randrange(len(Random)-1)]
Texto.write(palabra_inicial+' ')
palabra_actual=palabra_inicial
cont=1.0
while True:
	if palabra_actual==palabras('texto_a_leer.txt')[-1]:
		Texto.write(palabra_actual)
		Texto.write(' ')
		palabra_actual=choice(Random)
		continue
	a=palabra_despues_otra_posibilidades('texto_a_leer.txt',palabra_actual)
	b=list()
	if float(cont/97)==int(cont/97):
		Texto.write('.\n\n')
	for i in a:
		for x in range(a[i]):
			b.append(i)
	palabra_actual=choice(b)
	Texto.write(palabra_actual)
	Texto.write(' ')
	cont+=1
	if cont==291:
		Texto.write('.')
		break
Texto.close()
