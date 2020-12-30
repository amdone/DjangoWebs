from django.db import models


# Create your models here.
class Bili(models.Model):
    aid = models.IntegerField(primary_key=True, db_column='aid', blank=True, null=False, default=0)  # Field name made lowercase.
    created = models.IntegerField(db_column='created', blank=True, null=True)
    title = models.CharField(db_column='title', max_length=500, blank=True, null=True)
    description = models.CharField(db_column='description', max_length=500, blank=True, null=True)
    author = models.CharField(db_column='author', max_length=20, blank=True, null=True)
    mid = models.IntegerField(db_column='mid', blank=True, null=True)
    pic = models.CharField(db_column='pic', max_length=100, blank=True, null=True)
    remove = models.BooleanField(db_column='remove', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'bili'
