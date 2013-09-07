from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    SEXS_CONSTANTS = (
        ('m', 'Masculino'),
        ('f', 'Femenino'),
    )

    def __str__(self):
        return self.user.username

    web = models.URLField("Pagina web", max_length=100)
    phone = models.CharField("Numero Telefonico", max_length=11)
    user = models.ForeignKey(User, unique=True)
    sex = models.CharField("Sexo", max_length=1, choices=SEXS_CONSTANTS)
