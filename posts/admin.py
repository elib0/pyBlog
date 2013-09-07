from django.contrib import admin
from posts.models import Post, Categorie, Comment

admin.site.register(Post)
admin.site.register(Categorie)
admin.site.register(Comment)
