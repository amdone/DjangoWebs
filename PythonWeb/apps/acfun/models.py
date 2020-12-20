from django.db import models


# Create your models here.
class Acfun(models.Model):
    acno = models.CharField(db_column='acno', max_length=20, blank=True, null=True)  # Field name made lowercase.
    acerid = models.IntegerField(db_column='acerid', blank=True, null=True)
    acname = models.CharField(db_column='acname', max_length=20, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='title', max_length=40, blank=True, null=True)  # Field name made lowercase.
    uploadtime = models.IntegerField(db_column='uploadtime', blank=True,
                                     null=True)  # Field name made lowercase.
    cover = models.CharField(db_column='cover', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'acer'
