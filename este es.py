from funciones import *
import random

Random=palabras('texto_a_leer.txt')
Texto=open('texto_generado.txt','w')
palabra_inicial=Random[randrange(len(Random))]
write(palabra_inicial)

while True:

