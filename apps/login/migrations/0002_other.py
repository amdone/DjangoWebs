# Generated by Django 3.1.4 on 2020-12-20 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, db_column='name', max_length=20, unique=True)),
                ('left_count', models.IntegerField(blank=True, db_column='left_count')),
                ('other', models.CharField(blank=True, db_column='other', max_length=200, null=True)),
            ],
            options={
                'db_table': 'other',
                'managed': True,
            },
        ),
    ]
