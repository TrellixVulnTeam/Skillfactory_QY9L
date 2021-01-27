from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=255, null=False)
    rating = models.IntegerField(default=0)
    username = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        # return f'Author:{self.name}, rating:{self.rating}'

    def update_rating(self):
        posts_rate = 0
        com_rate = 0
        cm_ps_rate = 0
        for ps in Post.objects.filter(author=self.pk):
            # print(f"Post({ps.pk}) rating:{ps.rating}")
            posts_rate += ps.rating*3
            for cm_ps in Comment.objects.filter(post=ps.pk):
                # print(f"Post({ps.pk}) comment({cm_ps.pk}) rating: {cm_ps.rating}")
                cm_ps_rate += cm_ps.rating
        for cm in Comment.objects.filter(user=self.pk):
            # print(f"Comment({cm.pk}) rating:{cm.rating}")
            com_rate += cm.rating
        overall_rating = posts_rate+com_rate+cm_ps_rate

        # print(f'----------\nPosts rating:{posts_rate}')
        # print(f'Comments rating:{com_rate}')
        # print(f'All Posts - Comments rating:{cm_ps_rate}')
        # print(f'----------\nOVERALL rating:{overall_rating}')
        self.rating = overall_rating
        self.save()



class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        # return f'[ID:{self.pk}], name:{self.name}'
        return self.name


class Post(models.Model):
    news = 'NE'
    articles = 'AR'
    CHOICE = [(news, 'Новость'), (articles, 'Статья')]

    type = models.CharField(max_length=2, choices=CHOICE, default='NE')
    create_date = models.DateTimeField(auto_now_add=True)
    header = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')

    def __str__(self):
        # return f"[ID={str(self.pk)}, TYPE={self.type}] - header={self.header} (rate:{self.rating})"
        return self.title

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[:124]+'...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.pk
        # return f'ID={self.pk}:({self.post.pk} -> {self.category.pk})\n'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.text
        # return f'User({self.user.username}) to post ({self.post.header[:25]}...): "{self.text[:25]}, rate: {self.rating}"'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
