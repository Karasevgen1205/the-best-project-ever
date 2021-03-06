# Generated by Django 3.1.3 on 2020-12-19 08:17

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0025_auto_20201219_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.RemoveField(
            model_name='book',
            name='users_like',
        ),
        migrations.RemoveField(
            model_name='testcomment1',
            name='test',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='book',
        ),
        migrations.AlterUniqueTogether(
            name='likebookuser',
            unique_together={('user', 'tmp_book')},
        ),
        migrations.DeleteModel(
            name='TestComment',
        ),
        migrations.DeleteModel(
            name='TestComment1',
        ),
        migrations.DeleteModel(
            name='TestTale',
        ),
        migrations.RemoveField(
            model_name='likebookuser',
            name='book',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
