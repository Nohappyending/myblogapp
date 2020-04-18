#from django.shortcuts import render

#from django.http import HttpResponse


#def index(request):
#    return HttpResponse("Hello, students. You're at the BLG.")
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
