from django.shortcuts import render, get_object_or_404
from .models import Post
import requests
from django.http import JsonResponse

# Create your views here.
def generate(request):
    if request.user.is_authenticated :
        res = requests.get("https://rhidwan.000webhostapp.com/wp-json/wp/v2/posts")
        posts = res.json()
        for i in range(len(posts)):
            po, name = Post.objects.update_or_create(title=str(posts[i]["title"]["rendered"]))
            po.created_at = str(posts[i]["date"])
            po.title = str(posts[i]["title"]["rendered"])
            po.slug = str(posts[i]["slug"])
            po.link = str(posts[i]["link"])
            po.content = str(posts[i]["content"]["rendered"])
            po.excerpt = str(posts[i]["excerpt"]["rendered"])
            po.save()
    return JsonResponse({'status':'success'})

def get_posts(request):
    posts = Post.objects.all()
    data = []
    for post in posts:
        data.append({
            "id": post.post_id,
            "created at": post.created_at ,
            "excerpt": {"rendered": post.excerpt},
            "title" : {"rendered": post.title},
            "content": {"rendered": post.content},
            "slug": post.slug,
            "link": post.link
        })
    return JsonResponse(data, safe=False)

def get_post(request,post_id):
    #pass
    post = get_object_or_404(Post, post_id=post_id)
    data = {
        "id": post.post_id,
        "created at": post.created_at,
        "excerpt": {"rendered": post.excerpt},
        "title" : {"rendered": post.title},
        "content": {"rendered": post.content},
        "slug": post.slug,
        "link": post.link
    }
    return JsonResponse(data, safe=False)
