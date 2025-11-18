import requests

def obtener_clima(driver, consulta):
    # Frase original → eliminar palabras irrelevantes
    stopwords = ["clima", "temperatura", "dime", "de", "la", "el", "hoy", "en", "quiero", "saber"]
    palabras = consulta.split()

    ciudad_filtrada = " ".join([p for p in palabras if p not in stopwords]).strip()

    # Si quedó vacío, usar la frase original
    if not ciudad_filtrada:
        ciudad_filtrada = consulta

    # Correcciones comunes
    ciudad_filtrada = ciudad_filtrada.replace("cdmx", "ciudad de mexico")

    # Buscar coordenadas
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={ciudad_filtrada}&count=1&language=es&format=json"
    geo = requests.get(geo_url).json()

    if "results" not in geo:
        return f"No pude encontrar la ciudad: {ciudad_filtrada}"

    lat = geo["results"][0]["latitude"]
    lon = geo["results"][0]["longitude"]
    nombre_ciudad = geo["results"][0]["name"]

    # Clima actual
    clima_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&timezone=auto"
    clima = requests.get(clima_url).json()

    temperatura = clima["current_weather"]["temperature"]
    viento = clima["current_weather"]["windspeed"]

    return f"El clima en {nombre_ciudad} es de {temperatura}°C con viento de {viento} km/h."
