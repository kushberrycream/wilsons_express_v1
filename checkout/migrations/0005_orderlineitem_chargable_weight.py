# Generated by Django 3.1.8 on 2021-06-02 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20210518_0048'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='chargable_weight',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
