# Generated by Django 4.1 on 2022-09-03 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram_clone', '0004_remove_feed_like_count_remove_feed_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True, unique=True, verbose_name='email'),
        ),
    ]
