from django.db import models

# Create your models here.


from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=20)
    groups = models.ManyToManyField('Group', through='Membership')


class Group(models.Model):
    name = models.CharField(max_length=20)


class Membership(models.Model):
    member = models.ForeignKey('Member')
    group = models.ForeignKey('Group')
    join_date = models.CharField(max_length=32)
