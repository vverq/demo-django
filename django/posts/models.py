from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return self.title


class Ip(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=0)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
