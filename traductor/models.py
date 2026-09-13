from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class SenaLSC(models.Model):
    TIPO = (
        ("palabra", "Palabra"),
        ("frase", "Frase"),
    )

    texto = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    archivo = models.FileField(upload_to="senas/")
    tipo = models.CharField(max_length=10, choices=TIPO)

    def __str__(self):
        return f"{self.texto} ({self.tipo})"
