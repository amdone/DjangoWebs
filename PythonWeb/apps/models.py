from django.db import models


# Create your models here.

class Tweets(models.Model):
    fuk_id = models.CharField(primary_key=True, db_column='Fuk_id', max_length=50, blank=True, null=False,
                              default='null')  # Field name made lowercase.
    twer_id = models.CharField(db_column='Twer_id', max_length=40, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=40, blank=True,
                                null=True)  # Field name made lowercase.
    createtime = models.CharField(db_column='CreateTime', max_length=25, blank=True,
                                  null=True)  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=500, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=10, blank=True,
                                null=True)  # Field name made lowercase.
    likes = models.CharField(db_column='Likes', max_length=10, blank=True, null=True)  # Field name made lowercase.
    retweets = models.CharField(db_column='Retweets', max_length=10, blank=True,
                                null=True)  # Field name made lowercase.
    imgs = models.CharField(db_column='Imgs', max_length=200, blank=True, null=True)  # Field name made lowercase.
    video = models.CharField(db_column='Video', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remove = models.BooleanField(db_column='remove', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tweets'
