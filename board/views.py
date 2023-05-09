from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post

# Create your views here.
# FBV(함수로 직접 지정해 주는 방법) 방식으로 만들어 본 거임
# def index(request):
#     posts = Post.objects.all().order_by('-pk')
# 
#     return render(
#         request,
#         'board/post_list.html',
#         {
#             'posts': posts,
#         }
#     )

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'board/post_detail.html',
        {
            'post': post,
        }
    )
