import unicodedata
import re

def sanitizar(texto):
    # Minúsculas
    texto = texto.lower()
    
    # Eliminar tildes usando NFD
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(
        c for c in texto 
        if unicodedata.category(c) != "Mn"
    )
    
    # Quitar caracteres especiales (solo letras, números y espacios)
    texto = re.sub(r"[^a-z0-9\s]", "", texto)
    
    return texto

def extraer_ciudad(texto):
    texto = sanitizar(texto)

    # Lista de palabras irrelevantes
    stopwords = {
        "dame","quiero","saber","como","esta","el","la","de","del",
        "clima","tiempo","en","por","favor","me","puedes","decir"
    }

    palabras = texto.split()

    # Filtrar palabras que sí podrían ser una ciudad
    palabras_filtradas = [p for p in palabras if p not in stopwords]

    if not palabras_filtradas:
        return None

    # Regla especial para CDMX
    if "cdmx" in palabras_filtradas:
        return "ciudad de mexico"

    # Reconstruir posible nombre de ciudad
    ciudad = " ".join(palabras_filtradas)

    # Mapa de equivalencias comunes
    equivalencias = {
        "mexico": "ciudad de mexico",
        "ciudad mexico": "ciudad de mexico",
        "ciudad de mexico": "ciudad de mexico",

        "jalisco": "jalisco",
        "guadalajara": "guadalajara",
        "veracruz": "veracruz",
        "monterrey": "monterrey",
        "puebla": "puebla",
        "guanajuato": "guanajuato",
    }

    # Normalizar ciudad detectada
    if ciudad in equivalencias:
        return equivalencias[ciudad]

    # Detección aproximada
    for k, v in equivalencias.items():
        if k in ciudad:
            return v

    return ciudad
