from django.shortcuts import render 
from .models import Post,Comment
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
#from .import CommentForm


# Create your views here.



def all_post(request):
    context = {}
    posts_list = Post.objects.filter(published=True)
    paginator = Paginator(posts_list, 2) 
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context['posts'] = posts

    return render(request, 'home.html' ,context)   



def postView(request, slug):
  template_name = 'post-page.html'
  context = {}
  post = Post.objects.get(slug=slug)
  context['post'] = post
  return render(request, template_name=template_name, context=context) 


def addComment(request):
  if request.method == 'POST':
    author = request.POST.get('name')
    message = request.POST.get('message')
    post_id = request.POST.get('post_id')
    next = request.POST.get('next')
    spam = Comment()
    spam.author = author
    spam.body = message
    spam.post = Post.objects.get(pk=post_id)
    spam.save()
    #TODO: add a success message
    return HttpResponseRedirect(next)