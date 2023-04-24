from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Post


# Create your views here.
'''CBV'''
class PostList(ListView):
    model = Post
    ordering = ('-pk')
    # PostList 클래스 이름을 기반으로 생성
    # 템플릿 : post_list.html
    # 페이지에서 사용할 데이터 : post_list

    # 템플릿 직접 지정
    # template_name = 'blog/index.html'

'''
def index(request):
    posts = Post.objects.all().order_by('-pk')
    return render(
        request,
        'blog/post_list.html',
        {
            'posts':posts
        }
    )
'''


class PostDetail(DetailView):
    model = Post


'''
def detail(request,pk):
    post = Post.objects.get(pk=pk)
    return render(
        request,
        'blog/post_detail.html',
        {'post':post},
    )
'''