# Generated by Django 2.2.3 on 2019-08-07 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('award_list', '0002_auto_20190805_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='award_list',
            name='award_no',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
