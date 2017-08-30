# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import (
    HttpResponse,
    JsonResponse,
)
from django.shortcuts import render
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
