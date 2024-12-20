from django.contrib.auth.models import User
from django.db import models


class SearchRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    search_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} searched for {self.username} at {self.search_time}"
