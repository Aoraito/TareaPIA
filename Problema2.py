
import string

def contar_palabras(lista_palabras, ruta):

    frecuencias = {}

    for palabra in lista_palabras:
        frecuencias[palabra.lower()] = 0

    
    with open(ruta, "r", encoding="utf-8") as archivo:
        texto = archivo.read()

    
    texto = texto.lower()

    
    for signo in string.punctuation:
        texto = texto.replace(signo, " ")

    
    palabras_texto = texto.split()

    
    for palabra in palabras_texto:
        if palabra in frecuencias:
            frecuencias[palabra] += 1

    
    return dict(sorted(frecuencias.items()))


palabras = ["hola", "python", "desde"]

resultado = contar_palabras(palabras, "textoProblema2.txt")

print(resultado)
