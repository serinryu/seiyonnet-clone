# Generated by Django 4.0.3 on 2022-03-08 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0013_remove_profile_like_posts_profile_like_anonyposts_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='freepost',
            name='like_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
