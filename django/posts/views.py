from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from posts.models import Post, Comment, Ip


def resume(request):
    return render(request, 'resume.html', {})


def index(request):
    posts = Post.objects.all()

    context = {
        "counts_views_and_comments": {post: [Comment.objects.filter(post_id=post.id).count(),
                                  Ip.objects.filter(post_id=post.id).count()] for post in posts},
    }
    return render(request, 'index.html', context)


def post(request, post_id):
    comments = Comment.objects.filter(post_id=post_id)
    paginator = Paginator(comments, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    ip = get_client_ip(request)
    Ip.objects.get_or_create(ip=ip, post_id=post_id)

    context = {
        "comments": page_obj,
        "post": Post.objects.get(id=post_id)
    }

    return render(request, 'post.html', context)


def create_comment(request, post_id):
    if request.method == "POST":
        text = request.POST['text']
        Comment.objects.create(text=text, post_id=post_id).save()
        return redirect("post", post_id=post_id)

    return render(request, 'create_comment.html', {})


def create_post(request):
    if request.method == "POST":
        title = request.POST['title']
        text = request.POST['text']
        Post.objects.create(title=title, text=text).save()
        return redirect("index")

    return render(request, 'create_post.html', {})


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
