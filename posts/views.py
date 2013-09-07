from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import simplejson
from posts.models import Post, Comment
from django.template import RequestContext
from datetime import datetime

def index(request):
    last_posts = Post.objects.filter(date__lt=datetime.now()).order_by('date').reverse()
    context = {'last_posts_list': last_posts}
    return render(request, 'index.html', context, context_instance=RequestContext(request))

def ajax_single_post(request, idpost):
    if request.is_ajax():                                       #Si no viene de llamada ajax
        especific_post = Post.objects.filter(pk=idpost)
        comments = Comment.objects.filter(post=idpost)
        context = {'especific_post': especific_post, 'post_comments': comments}
        return render(request, 'posts/single_post.html', context)
    else:                                                       #redirecciono si no es de ajax
        return redirect('home')

def single_post(request, idpost):
    especific_post = Post.objects.filter(pk=idpost)
    comments = Comment.objects.filter(post=idpost)
    context = {'especific_post': especific_post, 'post_comments': comments}
    return render(request, 'posts/single_post.html', context)


# Fomularios
def ajax_form_comment_post(request,idpost):
    msg = {'success': 0, 'message': ''}
    if request.is_ajax():
        p = Post.objects.get(pk=idpost)
        c = Comment( post = p, text=request.POST['comment'], date=datetime.now() )
        try:
            c.save()
            msg['success'] = 1
            msg['message'] = 'Comentario Insertado'
        except:
            msg['success'] = 0
            msg['message'] = 'Error al insertar el comentario'

    json = simplejson.dumps(msg)
    return HttpResponse(json, mimetype='application/json')
