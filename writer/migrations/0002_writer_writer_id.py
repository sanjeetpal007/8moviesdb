# Generated by Django 2.2.3 on 2019-08-05 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='writer',
            name='writer_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
