# Generated by Django 2.2.3 on 2019-08-05 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genre_name', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre_name',
            name='genre_name_id',
            field=models.IntegerField(),
        ),
    ]