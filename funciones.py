def cantidad_letras(text): #nope
    texto = open(text)     
    cantidad = dict()   
    for linea in texto: 
        palabras = linea.strip().split()
        for palabra in palabras:
            for i in range(len(palabra)):
                if palabra[i:i+1] not in cantidad:
                    cantidad[palabra[i:i+1]] = 1
                elif palabra[i:i+1] in cantidad:
                    cantidad[palabra[i:i+1]] += 1
    return cantidad

def letra_despues_otra_cantidad(text, l1, l2): # nope
    texto = open(text)
    cantidad = 0
    for linea in texto:
        palabras = linea.strip().split()
        for palabra in palabras:
            for i in range(len(palabra)-1):
                if palabra[i] == l1 and palabra[i+1] == l2:
                    cantidad += 1
    return cantidad

def palabras(text): #siquesi
    texto = open(text)      
    words = list()    
    for linea in texto:
        palabras = linea.strip().split(' ')
        for palabra in palabras:
            if palabra not in words:
                words.append(palabra)
    return words
        
def palabra_despues_otra_cantidad(text, p1, p2): #siquesi
    texto = open(text)
    cantidad = 0
    for linea in texto:
        palabras = linea.strip().split(' ')
        for i in range(len(palabras)-1):
            if palabras[i] == p1 and palabras[i+1] == p2:
                cantidad += 1
    return cantidad

def palabra_despues_otra_posibilidades(text, p1): #siquesi
    texto = open(text)
    words = dict()   
    for linea in texto:
        palabras = linea.strip().split()
        for i in range(len(palabras)-1):
            if palabras[i] == p1 and i != (len(palabras)-1):
                if palabras[i+1] not in words:
                    words[palabras[i+1]] = 1
                elif palabras[i+1] in words:
                    words[palabras[i+1]] += 1
    return words
                
def histograma(text): #siquesi
    lista = palabras(text)
    d = dict()
    for x in lista:
        for y in lista:
            d[(x,y)] = palabra_despues_otra_cantidad(text, x, y)
    return d

def transicion(text, h): #siquesi
    lista = palabras(text)
    d = dict()
    for palabra in lista:
        t = 0.0
        for k, v in h.items():
            x, y = k
            if x == palabra:
                t += float(v)
        for k, v in h.items():
            x, y = k
            if x == palabra:
                d[(x,y)] = float(h[(x,y)]) / t
    return d

def random (x,y,cantidad):
    import random
    num = random.choice(range(x,y))
    cantidad = random.choice(range(1,cantidad+1))

    return num,cantidad


























    
