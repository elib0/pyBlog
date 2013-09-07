from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categorie(models.Model):
    def __str__(self):
        return self.title + ': ' + self.description

    def get_title(self):
        return self.title

    title = models.CharField("Titulo", max_length=15)
    description = models.TextField("Descripcion")
    img = models.CharField("Url de la imagen", max_length=100, null=True, blank=True)

class Post(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField("Titulo", max_length=50)
    content = models.TextField("Contenido")
    categorie = models.ForeignKey(Categorie, verbose_name=u'Categoria')
    author = models.ForeignKey(User)
    # comment = models.ForeignKey(Comment, verbose_name=u'commentarios', blank=True, null=True)
    date = models.DateTimeField('Fecha de Publicacion')

class Comment(models.Model):
    def __str__(self):
        return self.text
    post = models.ForeignKey(Post)
    text = models.TextField("comentario")
    date = models.DateField("Fecha de publicacion")
