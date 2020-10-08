from django.http import HttpResponseRedirect
from django.shortcuts import render


from blogApp.models import BlogPost
from blogApp.forms import BlogPostForm
from django.urls import reverse


def post(request, blog_id):
    post = BlogPost.objects.get(id=blog_id)

    context = {'post': post}
    return render(request, 'post.html', context)


def edit_blog_post(request, blog_id):
    post = BlogPost.objects.get(id=blog_id)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = BlogPostForm(instance=post)
    else:
        # POST data submitted; process data.
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog_post', args=[blog_id]))

    context = {'post': post, 'form': form}
    return render(request, 'edit_blog_post.html', context)


def new_blog_post(request):
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BlogPostForm()
    else:
        # POST data submitted; process data.
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))

    context = {'form': form}

    return render(request, 'new_blog_post.html', context)


def blog_posts(request):
    posts = BlogPost.objects.all().order_by('-date_added')

    context = {
        'posts': posts
    }

    return render(request, 'blog_posts.html', context)


def index(request):
    return render(request, 'index.html')