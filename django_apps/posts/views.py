# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib import messages

from rest_framework.generics import (
	ListAPIView,
	RetrieveAPIView,
	DestroyAPIView,
	UpdateAPIView,
)

from .serializers import PostDetailSerializer, PostListSerializer
from .forms import PostForm

# Create your views here.

def post_create(request): #C
	form = PostForm(request.POST or None) #Built in validation from forms
	if form.is_valid(): #if all fields filled out then save
		# print(form.cleaned_data.get("title")) #print field
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Sucessfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	# form = PostForm()
	# if request.method == "POST":
	# 	print request.POST.get("title")
	# 	print request.POST.get("content")
	# 	# Post.objects.create(title="title") #DONOT DO THIS!
	return render(request, "post_form.html", context)

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
	return render(request, "post_list.html", context)

def post_update(request, id=None): #U
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>Item</a> Success!", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"title": instance.title,
		"instance": instance,
		"form": form,
	}
	return render(request, "post_form.html", context)

def post_delete(request, id=None): #D
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request, "Sucessfully Deleted", extra_tags='html_safe')
	return redirect("posts:index")

def post_home(request): #C
	context = {
		"title": "Welcome to Bambo's Blog"
	}
	return render(request, "index.html", context)

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

