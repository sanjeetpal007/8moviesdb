# Generated by Django 2.2.3 on 2019-08-11 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('episode', '0005_remove_episode_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='adult',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]