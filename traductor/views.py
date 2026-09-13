import speech_recognition as sr
import os
import unicodedata
from django.conf import settings
from django.shortcuts import render

print(sr.Microphone.list_microphone_names())

# Función para eliminar tildes
def quitar_tildes(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def escuchar_microfono(request):
    estado = ""
    texto = ""
    imagenes_encontradas = []

    if request.method == "POST":
        estado = "Escuchando..."

        r = sr.Recognizer()

        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.5)
                r.energy_threshold = 300
                audio = r.listen(source)

            texto = r.recognize_google(audio, language="es-CO")
            estado = "Texto detectado"


            texto_normalizado = quitar_tildes(texto.lower())
            palabras = texto_normalizado.split()

            carpeta = os.path.join(settings.MEDIA_ROOT, "senas")

            for palabra in palabras:
                palabra_normalizada = quitar_tildes(palabra.lower().strip())

                for root, dirs, files in os.walk(carpeta):
                    for archivo in files:
                        nombre, ext = os.path.splitext(archivo)
                        nombre_normalizado = quitar_tildes(nombre.lower().strip())

                        if palabra_normalizada in nombre_normalizado:
                            ruta_relativa = os.path.relpath(os.path.join(root, archivo), settings.MEDIA_ROOT)
                            imagenes_encontradas.append(ruta_relativa)

        except Exception as e:
            estado = f"Error: {str(e)}"

    return render(request, "microfono.html", {
        "estado": estado,
        "texto": texto,
        "imagenes": imagenes_encontradas
    })
