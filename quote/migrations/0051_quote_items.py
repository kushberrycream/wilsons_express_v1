# Generated by Django 3.1.8 on 2021-04-28 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0050_auto_20210428_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='items',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
