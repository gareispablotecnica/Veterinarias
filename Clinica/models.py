from django.db import models

class Mascota(models.Model):
    ESPECIES = [
        ('Perro', 'Perro'),
        ('Gato', 'Gato'),
        ('Ave', 'Ave'),
        ('Roedor', 'Roedor'),
        ('Reptil', 'Reptil'),
        ('Otro', 'Otro'),
    ]

    ID_Mascota = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Especie = models.CharField(max_length=20, choices=ESPECIES)
    Raza = models.CharField(max_length=50, blank=True)
    Edad = models.IntegerField()
    Dueno = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=20)
    Foto = models.ImageField(upload_to='mascotas/', blank=True, null=True)
    Fecha_Registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Nombre} - {self.Dueno}"
