from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.
class PostList(ListView):
    model = Post
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post
    
# def index(request):
    
#     posts = Post.objects.all().order_by('-pk')
    
#     datas = '블로그 데이터 입니다.'
    
#     return render(
#         request,
#         'blog/index.html',
#         {
#             'datas':datas,
#             'posts':posts,
#         }
#     )

# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
    
#     return render(
#         request,
#         'blog/single_post_page.html',
#         {
#             'post':post,
#         }
#     )