from django.db import models

class FileManager(models.Model):
    name = models.CharField(max_length=255, unique=True)
    file = models.FileField()
    user = models.ForeignKey('account.User',on_delete=models.SET_NULL,null=True,related_name='files')