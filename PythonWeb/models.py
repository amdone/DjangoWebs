# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Tweets(models.Model):
    fuk_id = models.CharField(db_column='Fuk_id', max_length=50, blank=True, null=True)  # Field name made lowercase.
    twer_id = models.CharField(db_column='Twer_id', max_length=40, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=40, blank=True, null=True)  # Field name made lowercase.
    createtime = models.CharField(db_column='CreateTime', max_length=25, blank=True, null=True)  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=500, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=10, blank=True, null=True)  # Field name made lowercase.
    likes = models.CharField(db_column='Likes', max_length=10, blank=True, null=True)  # Field name made lowercase.
    retweets = models.CharField(db_column='Retweets', max_length=10, blank=True, null=True)  # Field name made lowercase.
    imgs = models.CharField(db_column='Imgs', max_length=200, blank=True, null=True)  # Field name made lowercase.
    video = models.CharField(db_column='Video', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tweets'


