# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Listing(models.Model):
	item_name = models.CharFields(max_length=30)
	item_img = models.CharFields(max_length=30)
