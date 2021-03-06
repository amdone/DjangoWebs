from django.db import models
import datetime


# Create your models here.
class Acfun(models.Model):
    # id = models.UUIDField(db_column='id', blank=False, unique=True, null=False, primary_key=True)
    acno = models.CharField(primary_key=True, db_column='acno', max_length=20, blank=True,
                            null=False, default='null')  # Field name made lowercase.
    acerid = models.IntegerField(db_column='acerid', blank=True, null=True)
    acname = models.CharField(db_column='acname', max_length=20, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='title', max_length=40, blank=True, null=True)  # Field name made lowercase.
    uploadtime = models.IntegerField(db_column='uploadtime', blank=True,
                                     null=True)  # Field name made lowercase.
    cover = models.CharField(db_column='cover', max_length=100, blank=True, null=True)  # Field name made lowercase.
    remove = models.BooleanField(db_column='remove', blank=True, null=True)

    def __str__(self):
        return "{}/{}/{}/{}".format(self.acno, self.acname, self.title, self.uploadtime)

    class Meta:
        managed = True
        db_table = 'acer'
        ordering = ['-uploadtime']
