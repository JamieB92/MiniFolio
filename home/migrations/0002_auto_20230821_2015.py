# Generated by Django 3.2.20 on 2023-08-21 20:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomments',
            name='post_comments',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comment', to='home.userposts'),
        ),
        migrations.AlterField(
            model_name='userposts',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
