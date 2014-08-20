def cantidad_letras(t): # RETORNA DICCIONARIO CON LAS LETRAS Y LAS VECES QUE RE REPITE
    texto = open(t)     # INCLUYE SIMBOLOS
    cantidad = dict()   # NO INCLUYE LETRA 'ENIE' NI VOCALES CON TILDE
    for linea in texto: # PIDE COMO ENTRADA UN ARCHIVO .TXT
        palabras = linea.strip().split()
        for palabra in palabras:
            for i in range(len(palabra)):
                if palabra[i:i+1] not in cantidad:
                    cantidad[palabra[i:i+1]] = 1
                elif palabra[i:i+1] in cantidad:
                    cantidad[palabra[i:i+1]] += 1
    return cantidad

def cantidad_palabras(t):# PIDE COMO ENTRADA UN ARCHIVO.TXT
    texto = open(t)      # INCLUYE SIMBOLOS COMO PARTE DE LA PALABRA (por solucionar)
    cantidad = dict()    # RETORNA UN DICCIONARIO CON LAS PALABRAS Y SU NUMERO DE REPETICIONES
    for linea in texto:
        palabras = linea.strip().split()
        for palabra in palabras:
            if palabra not in cantidad:
                cantidad[palabra] = 1
            elif palabra in cantidad:
                cantidad[palabra] += 1
    return cantidad
