# Generated by Django 2.2.3 on 2019-08-11 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subtitle_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle_list_id', models.PositiveIntegerField()),
                ('subtitle_no', models.PositiveIntegerField()),
                ('subtitle_name_id', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name_plural': 'subtitle list',
            },
        ),
    ]
