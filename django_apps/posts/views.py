# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

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
	form = PostForm(request.POST or None, request.FILES or None) #Built in validation from forms
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

def post_detail(request, slug=None): #R
	instance = get_object_or_404(Post, slug=slug)
	context = {
		"title": instance.title,
		"instance": instance,
	}
	return render(request, "post_detail.html", context)

def post_list(request):
	queryset_list = Post.objects.all()
	paginator = Paginator(queryset_list, 7) # Show 25 contacts per page
	page = request.GET.get('page')
	page_request_var = 'page'
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)
	context = {
		"object_list": queryset,
		"title":"List",
		"page_request_var": page_request_var,
	}
	return render(request, "post_list.html", context)

def post_update(request, slug=None): #U
	instance = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
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

def post_delete(request, slug=None): #D
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	messages.success(request, "Sucessfully Deleted", extra_tags='html_safe')
	return redirect("posts:list")

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

