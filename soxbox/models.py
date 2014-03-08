from django.contrib import auth
from django.contrib.auth.models import User
from django.db import models

class Media(models.Model):
    user = models.ForeignKey(User)
    file_name = models.CharField(max_length=1000)
    file = models.FileField(upload_to="my_media_manager")
    created_date = models.DateTimeField(auto_now=True, editable=False)

    def __unicode__(self):
        return self.file_name

