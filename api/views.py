# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Post
from api.serializers import PostSerializer



@api_view()
def post_detail(request, pk):
    posts = Post.objects.filter(id=pk)
    if not posts:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    post = posts.first()
    serializer = PostSerializer(post)
    return Response(serializer.data)


@api_view()
def post_list(request):
    posts = Post.objects.all()
    serialized_posts = []
    for post in posts:
        serialized_posts.append(PostSerializer(post).data)
    response = {
        "posts": serialized_posts,
    }
    return Response(response)

@api_view(http_method_names=['POST'])
def post_create(request):
    serializer = PostSerializer(data=request.POST)
    if serializer.is_valid():
        MSG = "successfully created the post"
        data = serializer.save()
    else:
        MSG = "There's something wrong with submitted data"
    response = {
        'message': MSG,
    }
    return Response(response)

