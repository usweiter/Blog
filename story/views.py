from django.shortcuts import render, redirect
from .forms import FormAddStory
from django.contrib.auth.decorators import login_required

@login_required
def add_story(request):
    if request.user.is_superuser:

        form = FormAddStory()
        if request.method == 'POST':
            form = FormAddStory(data=request.POST, files=request.FILES)
            if form.is_valid():
                story = form.save(commit=False)
                story.author = request.user
                story.save()
                return redirect('/')    
        return render(request, 'story/add_story.html', {'form':form})
    else:
        return redirect('/')