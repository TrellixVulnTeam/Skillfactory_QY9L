from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length = 255)
    rating = models.IntegerField()
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    def update_rating(self):
        pass


class Category(models.Model):
    name = models.CharField(max_length = 128, unique=True)


class Post(models.Model):
    post_is_news = models.BooleanField(default=True)
    post_create_date = models.DateTimeField(null=False)
    post_header = models.CharField(max_length=255)
    post_text = models.TextField()
    post_rating = models.IntegerField(default=0)
    post_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_category = models.ManyToManyField(Category, through='PostCategory')
    def like(self):
        self.post_rating += 1
    def dislike(self):
        self.post_rating -= 1
    def preview(self):
        pass

class PostCategory(models.Model):
    post = models.ManyToManyField(Post, on_delete=models.SET_NULL)
    category = models.ManyToManyField(Category)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=2048)
    create_time = models.DateTimeField(null=False)
    rating = models.IntegerField(default=0)
    def like(self):
        self.rating += 1
    def dislike(self):
        self.rating -= 1
