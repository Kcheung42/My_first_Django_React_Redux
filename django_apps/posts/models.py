# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify

def upload_location(instance, filename):
	return "%s/%s" %(instance.id, filename)

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=120)
	slug = models.SlugField(unique=True)
	image = models.ImageField(null=True, blank=True,
						   height_field="img_height",
						   width_field="img_width",
						   upload_to=upload_location
						   )
	img_height = models.IntegerField(default=0)
	img_width= models.IntegerField(default=0)
	content = models.TextField(max_length=1000)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"slug" : self.slug})
		# return reverse("posts:detail", kwargs={"id" : self.id})

	def get_delete_url(self):
		return reverse("posts:delete", kwargs={"slug" : self.slug})
		# return reverse("posts:delete", kwargs={"id" : self.id})

	def get_edit_url(self):
		return reverse("posts:edit", kwargs={"slug" : self.slug})
		# return reverse("posts:edit", kwargs={"id" : self.id})
	# return "/posts/%s" %(self.id)

	class Meta:
		ordering = ["-timestamp", "-updated"]


def create_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = Post.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Post)
