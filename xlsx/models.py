from django.db import models
from django.contrib.auth.models import User


class Xlsx(models.Model):
    file_name = models.FileField(upload_to='Xlsx')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)
    ### изменить
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'File id: {self.id}'


