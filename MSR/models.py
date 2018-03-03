# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class videoMetaData(models.Model):
	"""docstring for videoMetaData"""
	title = models.IntegerField()
	comments = models.TextField()
	method1 = models.IntegerField(default='0')
	# category = models.TextField()
	
	# def __str__(self):
	# 	return self.title
		