from django.db import models

# Create your models here.

class Senator(models.Model):
    last_name = models.CharField(max_length=200)
    contact_form_url = models.CharField(max_length=1024)
