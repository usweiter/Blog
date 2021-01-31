from django.shortcuts import render
from post.models import ModelPost

def share_email(request, link):
    sent = False

    if request.method == 'POST':
        form = FormEmailPost(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            mail_title = f"Look at that, dude:\n\nFrom:{cd['name']}:{post.title}"
            mail_body = f"{post.text}\n\n{cd['comments']}"
            mail = send_mail(mail_title, mail_body, cd['sender'], [cd['to']])
            sent = True

            return render(request, 'post/post.html', {'post':post})
    else:
        form = FormEmailPost()

        return render(request, 'post/email_post.html', {'form':form, 'sent':sent})