# Generated by Django 3.1.4 on 2021-02-28 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0006_auto_20210228_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='c_company',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='quote',
            name='c_contact_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='quote',
            name='c_county',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='quote',
            name='c_email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='quote',
            name='c_phone_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='quote',
            name='c_street_address1',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='quote',
            name='c_street_address2',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='quote',
            name='c_town_or_city',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='quote',
            name='d_company',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='quote',
            name='d_contact_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='quote',
            name='d_county',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='quote',
            name='d_email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='quote',
            name='d_phone_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='quote',
            name='d_street_address1',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='quote',
            name='d_street_address2',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='quote',
            name='d_town_or_city',
            field=models.CharField(max_length=40),
        ),
    ]
