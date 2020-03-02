# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class AddressBookApplication(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    phone_number = models.IntegerField(max_length=12)
    email_address = models.EmailField(max_length=200, unique=True)
    zip_code = models.IntegerField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    notes = models.TextField(max_length=500, blank=True)





    
    

