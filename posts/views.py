from django.shortcuts import render

# Create your views here.
from posts.models import Post
from django.core.paginator import Paginator


def post_list_view (request):
    posts=Post.objects.filter(published=True)
    
    paginator = Paginator(posts, 5)
    
    if 'page' in request.GET.keys():
        page = paginator.page(request.GET['page'])
    else:
        page = paginator.page(1)
    print(request.GET)
    
    context={'page':'posts', 'page_object': page}
    return render(request, "posts/post_list.html",context)