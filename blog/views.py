from django.shortcuts import render, get_object_or_404
from .models import Posts

def show_blog(request):
    posts = Posts.objects.all()
    title = Posts.title
    text = Posts.text
    date = Posts.date
    image = Posts.image
    context = {
        'title': title,
        'text': text,
        'date': date,
        'image': image,
        'posts': posts,
    }
    return render(request, 'blog/blog.html', context)

def post_details(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)
    return render(request, 'blog/details.html', {'post': post})
