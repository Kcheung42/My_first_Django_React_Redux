# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post

from rest_framework.generics import (
		ListAPIView,
		RetrieveAPIView,
		DestroyAPIView,
		UpdateAPIView,
	)

from .serializers import PostDetailSerializer, PostListSerializer

# Create your views here.

def post_create(request): #C
	return HttpResponse("<h1>Hello</h1>")

def post_detail(request, id=None): #R
	instance = get_object_or_404(Post, id=id)
	context = {
			"title": instance.title,
			"instance": instance,
			}
	return render(request, "post_detail.html", context)

def post_list(request):
	queryset = Post.objects.all
	context = {
			"object_list": queryset,
			"title":"List",
			}
	return render(request, "index.html", context)

def post_update(request): #U
	return HttpResponse("<h1>Welcome to Update</h1>")

def post_delete(request): #D
	return HttpResponse("<h1>Welcome to delete</h1>")

def post_home(request): #C
	context = {
			"title": "Home"
			}
	return render(request, "index.html", context)
# return HttpResponse("<h1>Hello</h1>")

# Below are views for Rest API

class PostListAPIView(ListAPIView):
	serializer_class = PostListSerializer #Turn model into Json
	queryset = Post.objects.all() #must have queryset or overide get_querset() method
	lookup_field = 'id'

	# search_fields = ['title']
	# def get_queryset(self, *args, **kwargs):
	# 	queryset_list = Post.objects.all()
	# 	query = self.request.Get.get("q")
	# 	if query:
	# 		query_list = queryset_list.filter(
	# 				Q(title__icontains=query)).distinct()
	# 	return query_list

class PostDetailAPIView(RetrieveAPIView):
	serializer_class = PostDetailSerializer
	queryset = Post.objects.all()
	lookup_field = 'id'

