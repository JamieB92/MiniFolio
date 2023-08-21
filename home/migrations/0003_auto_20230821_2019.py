# Generated by Django 3.2.20 on 2023-08-21 20:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_auto_20230821_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomments',
            name='post_comments',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='home.userposts'),
        ),
        migrations.AlterField(
            model_name='userposts',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
