# Generated by Django 2.2.3 on 2019-08-03 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='writer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer_name', models.CharField(max_length=40)),
                ('image_id', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
