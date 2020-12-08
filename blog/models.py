from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Articles (models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    article = models.CharField(max_length = 500)
    picture = models.ImageField(upload_to = 'Images', null = True)

    def getLikes(self):
        return self.Likes.users.count()

    def getDisLikes(self):
        return self.DisLikes.users.count()

    def __str__(self):
        return self.user.username

class Likes (models.Model):
    user = models.ForeignKey(User, on_delete =models.CASCADE )
    article = models.OneToOneField(Articles , on_delete = models.CASCADE)

    def __str__(self):
        return self.article.article

class DisLikes (models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE )
    article = models.OneToOneField(Articles , on_delete = models.CASCADE)

    def __str__(self):
        return self.article.article



class Comments(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    article = models.ForeignKey(Articles, on_delete = models.CASCADE)
    comment = models.CharField(max_length = 100)

    def __str__(self):
        return self.user.username

class Replies(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    comment = models.ForeignKey(Comments, on_delete = models.CASCADE)
    reply = models.CharField(max_length = 100)

    def __str__(self):
        return self.user.username
