# Generated by Django 3.1.4 on 2020-12-03 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_remove_comment_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='manager.book'),
            preserve_default=False,
        ),
    ]
