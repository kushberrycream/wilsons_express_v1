# Generated by Django 3.1.4 on 2021-03-11 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0039_auto_20210311_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='height1',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='height2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='height3',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='height4',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='length1',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='length2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='length3',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='length4',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='weight2',
            field=models.DecimalField(blank=True, decimal_places=2, help_text="Max 30kg's", max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='weight3',
            field=models.DecimalField(blank=True, decimal_places=2, help_text="Max 30kg's", max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='weight4',
            field=models.DecimalField(blank=True, decimal_places=2, help_text="Max 30kg's", max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='width1',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='width2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='width3',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='width4',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
