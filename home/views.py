from django.shortcuts import render, get_object_or_404
from post.models import ModelPost
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag
from django.contrib.auth.decorators import login_required
from story.models import ModelStory
from django.contrib.auth.models import User
from django.conf import settings
from post.forms import FormAddPost, FormFastAddPost

@login_required
def home(request, tag=None):
    superuser = User.objects.get(username=settings.SUPERUSER_USERNAME)

    post_list = ModelPost.issued.all()
    stories = ModelStory.objects.filter(author=superuser)[:4]

    paginator = Paginator(post_list, 4)
    page = request.GET.get('page')

    form = FormFastAddPost()

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        
    return render(request, 'home/home.html', {
        'page':page,
        'posts':posts,
        'stories':stories,
        'form':form
        })