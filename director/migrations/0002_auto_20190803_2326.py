# Generated by Django 2.2.3 on 2019-08-03 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('director', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='image_id',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
