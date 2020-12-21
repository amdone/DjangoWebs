# login/models.py

from django.db import models


class User(models.Model):
    '''用户表'''

    id = models.AutoField(db_column='id', blank=False, unique=True, null=False, primary_key=True)
    name = models.CharField(db_column='name', max_length=20, blank=True, unique=True)
    password = models.CharField(db_column='password', max_length=20, blank=True, null=True)
    email = models.CharField(db_column='email', max_length=50, blank=True, null=True)
    sex = models.CharField(db_column='sex', max_length=5, blank=True, null=True)
    c_time = models.DateTimeField(db_column='c_time', max_length=30, blank=True, null=True)
    level = models.IntegerField(db_column='level', blank=True, default=0)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'login_user'
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'


class Other(models.Model):
    '''用户表'''

    id = models.AutoField(db_column='id', blank=False, unique=True, null=False, primary_key=True)
    name = models.CharField(db_column='name', max_length=20, blank=True, unique=True)
    left_count = models.IntegerField(db_column='left_count', blank=True)
    other = models.CharField(db_column='other', max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'other'

