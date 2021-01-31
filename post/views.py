from django.shortcuts import render, get_object_or_404, redirect
from .models import ModelPost
from .forms import FormAddPost
from django.core.mail import send_mail
from django.conf import settings
from comments.forms import FormComment
from comments.models import ModelComment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag
from django.db.models import Count

def post(request, id):
    post = get_object_or_404(ModelPost, id=id, status='published')

    if request.method == 'POST' and request.user.is_authenticated:
        form_comment = FormComment(request.POST)
        user = request.user

        if form_comment.is_valid():
            comment = form_comment.save(commit=False)
            comment.post = post
            comment.author = user
            comment.save()

            comment_list = ModelComment.objects.filter(post=post, active=True)
            return redirect(post, id=post.id)
    else:
        form_comment = FormComment()
        comment_list = ModelComment.objects.filter(post=post, active=True)
        
        post_tag_ids = post.tags.values_list("id", flat=True)
        related_post_list = ModelPost.objects.filter(tags__in=post_tag_ids).exclude(id=post.id)
        related_post_list = related_post_list.annotate(quantity_tags=Count("tags"))\
        .order_by("-quantity_tags", "-published")[:4]

    return render(request, 'post/post.html', {
        'post':post,
        'form_comment':form_comment,
        'comment_list':comment_list,
        'related_post_list':related_post_list,
        })

def posts_by_tag(request, tag=None):
    if tag:
        tag_obj = get_object_or_404(Tag, slug=tag)
        post_list = ModelPost.objects.filter(tags__in=[tag_obj])

    else:
        post_list = ModelPost.objects.filter()

    paginator = Paginator(post_list, 4)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'post/posts_by_tag.html', {
        'posts':posts,
        'page':page,
        'tag':tag})

@login_required
def add_post(request):
    if request.user.is_superuser:
        form = FormAddPost()
        
        if request.method == 'POST':
            form = FormAddPost(data=request.POST, files=request.FILES)
            
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user

                post.save()
                form.save_m2m()
                return redirect('/')
                
        return render(request, 'post/add_post.html', {'form':form})
        
    else:
        return redirect('/')