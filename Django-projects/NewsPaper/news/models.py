from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    author_name = models.CharField(max_length=255, null=False)
    rating = models.IntegerField(default=0)
    username = models.OneToOneField(User, on_delete=models.CASCADE)

    def update_rating(self):
        pass


class Category(models.Model):
    cat_name = models.CharField(max_length=128, unique=True)


class Post(models.Model):
    news = 'NE'
    articles = 'AR'
    CHOICE = [(news, 'Новость'), (articles, 'Статья')]

    post_is_news = models.CharField(max_length=1, choices=CHOICE, default=news)
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
        return self.post_text[0:100]


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(null=True)
    create_time = models.DateTimeField(null=False)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1

    def dislike(self):
        self.rating -= 1
