from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from blog.models import Post
from .serializers import PostSerializer
# Create your views here.

def PostList(ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    pass

def PostDetail(RetrieveDestroyAPIView):
    pass