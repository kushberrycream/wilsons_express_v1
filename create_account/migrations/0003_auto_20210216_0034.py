# Generated by Django 3.1.4 on 2021-02-16 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_account', '0002_auto_20210216_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create_account',
            name='freight',
            field=models.CharField(choices=[('mechanical', 'Mechanical'), ('plants_botanical', 'Plants and Botanical'), ('live_fish', 'Live Fish'), ('perishable', 'Perishable Items'), ('alcohol', 'Alcohol'), ('Other', 'Other Please Specify')], max_length=250),
        ),
    ]
