from django.db import models


# Create your models here.
class Comments(models.Model):
    """评论表"""
    id = models.AutoField(db_column='id', blank=False, unique=True, null=False, primary_key=True)
    to_id = models.IntegerField(db_column='to_id', blank=True, null=True)
    user_id = models.IntegerField(db_column='user_id', blank=True, null=False)
    user_name = models.CharField(db_column='user_name', max_length=20, blank=True, null=True)
    comment = models.CharField(db_column='comment', max_length=500, blank=True, null=True)
    c_time = models.DateTimeField(db_column='c_time', blank=True, null=True)
    likes = models.IntegerField(db_column='likes', blank=True, null=True, default=0)

    def __str__(self):
        return "id:{}/{}/{}/{}".format(self.id, self.user_name, str(self.c_time)[:19], self.comment)

    class Meta:
        managed = True
        db_table = 'comments'
