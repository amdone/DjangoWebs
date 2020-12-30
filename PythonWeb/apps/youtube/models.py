from django.db import models


# Create your models here.

class Youtube(models.Model):
    videoid = models.CharField(primary_key=True, db_column='videoId', max_length=20, blank=True, null=False,default='null')
    channelid = models.CharField(db_column='channelId', max_length=20, blank=True, null=True)
    uploadtime = models.CharField(db_column='upTime', max_length=20, blank=True, null=True)
    title = models.CharField(db_column='title', max_length=500, blank=True, null=True)
    video = models.CharField(db_column='video', max_length=60, blank=True, null=True)
    cover = models.CharField(db_column='cover', max_length=60, blank=True, null=True)
    description = models.CharField(db_column='description', max_length=500, blank=True, null=True)
    channeltitle = models.CharField(db_column='channelTitle', max_length=50, blank=True, null=True)
    userid = models.CharField(db_column='userId', max_length=40, blank=True, null=True)
    remove = models.BooleanField(db_column='remove', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'youtube'
