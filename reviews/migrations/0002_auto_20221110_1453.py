# Generated by Django 3.2.16 on 2022-11-10 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='review_title',
        ),
        migrations.AlterField(
            model_name='review',
            name='review_rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=5),
        ),
    ]
