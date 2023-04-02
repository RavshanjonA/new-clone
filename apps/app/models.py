from django.db import models
from apps.common.models import Base
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    followers = models.ManyToManyField('self', related_name='followings', symmetrical=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class UserProfile(Base):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_picture", null=True, default="default.jpg")
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(max_length=400, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)

from django.db.models import ForeignKey, TextField, CASCADE, FileField, Model, DateTimeField, BooleanField, \
    IntegerField, CharField

from apps.common.models import Base
from apps.choices import NotoificationChoice
from apps.utils import post_upload_path, validate_file_extension


class Post(Base):
    author = ForeignKey('user.User', on_delete=CASCADE, related_name="posts")
    title = CharField(max_length=128, null=True, blank=True)

    class Meta:
        db_table = "posts"


class PostMedia(Model):
    file = FileField(upload_to=post_upload_path, null=False, blank=False,
    validators = [validate_file_extension, ])
    post = ForeignKey('Post', on_delete=CASCADE, related_name="post_medias")


class Like(Model):
    user = ForeignKey('User', on_delete=CASCADE)
    created = DateTimeField(auto_now=True)
    post = ForeignKey('Post', on_delete=CASCADE, related_name='likes')

    class Meta:
        db_table = "likes"


class Comment(Model):
    post = ForeignKey('Post', related_name='comments', on_delete=CASCADE)
    body = TextField(max_length=500, )
    is_reply = BooleanField(default=False)
    author = ForeignKey('user.User', on_delete=CASCADE, related_name='comments')
    created_at = DateTimeField(auto_now_add=True)
    like = IntegerField(default=0)

    class Meta:
        ordering = ['like']
        db_table = "comments"


class Notification(Model):
    user = ForeignKey('User', on_delete=CASCADE)
    type = CharField(max_length=22, choices=NotoificationChoice.choices)
    is_seen = BooleanField(default=False)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "notfications"
        ordering = ['is_seen']
