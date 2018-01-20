from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, Group

class Person(User):
    class Meta:
        proxy = True
        ordering = ('first_name', )

    def __str__(self):
        return str(self.username)

    def validate_password(self, value: str) -> str:
        return make_password(value)


# class Folder(models.Model):
#     name = models.TextField()
#     parent = models.IntegerField(null=True, blank=True)
#     author = models.ForeignKey(Person, null=True, blank=True, related_name='folders', on_delete=models.CASCADE,)
#     is_root = models.BooleanField(blank=True)

#     def __str__(self):
#         return str(self.name)

class Hashtag(models.Model):
    name = models.TextField(max_length=30)
    # parent = models.IntegerField(null=True, blank=True)
    author = models.ForeignKey(Person, null=True, blank=True, related_name='hashtags', on_delete=models.CASCADE,)
    # is_root = models.BooleanField(blank=True)

    def __str__(self):
        return str(self.name)


class Note(models.Model):
    # parent = models.IntegerField(null=True)
    name = models.TextField()
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True, blank=True)
    # folder = models.ForeignKey(Hashtag, null=True, blank=True, related_name='notes', on_delete=models.CASCADE,)
    hashtags = models.ManyToManyField(Hashtag, blank=True, null=True)
    author = models.ForeignKey(Person, null=True, blank=True, related_name='notes', on_delete=models.CASCADE,)

    def __str__(self):
        return str(self.name)

class Questionnaire(models.Model):
    color = models.BooleanField()
    hashtag = models.BooleanField()
    i18n = models.BooleanField()
    importance = models.BooleanField()
    text = models.TextField()
    author = models.ForeignKey(Person, null=True, blank=True, related_name='questions', on_delete=models.CASCADE,)