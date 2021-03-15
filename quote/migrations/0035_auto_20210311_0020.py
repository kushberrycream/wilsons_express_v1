# Generated by Django 3.1.4 on 2021-03-11 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0034_auto_20210308_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='height1',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=7),
        ),
        migrations.AddField(
            model_name='quote',
            name='height2',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=7),
        ),
        migrations.AddField(
            model_name='quote',
            name='height3',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=7),
        ),
        migrations.AddField(
            model_name='quote',
            name='height4',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=7),
        ),
        migrations.AddField(
            model_name='quote',
            name='length1',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=7),
        ),
        migrations.AddField(
            model_name='quote',
            name='length2',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=7),
        ),
        migrations.AddField(
            model_name='quote',
            name='length3',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=7),
        ),
        migrations.AddField(
            model_name='quote',
            name='length4',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=7),
        ),
        migrations.AddField(
            model_name='quote',
            name='volume_weight1',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=7),
        ),
        migrations.AddField(
            model_name='quote',
            name='volume_weight2',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=7),
        ),
        migrations.AddField(
            model_name='quote',
            name='volume_weight3',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=7),
        ),
        migrations.AddField(
            model_name='quote',
            name='volume_weight4',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=7),
        ),
        migrations.AddField(
            model_name='quote',
            name='weight1',
            field=models.DecimalField(decimal_places=2, default='0', help_text="Max 30kg's", max_digits=5),
        ),
        migrations.AddField(
            model_name='quote',
            name='weight2',
            field=models.DecimalField(decimal_places=2, default='0', help_text="Max 30kg's", max_digits=5),
        ),
        migrations.AddField(
            model_name='quote',
            name='weight3',
            field=models.DecimalField(decimal_places=2, default='0', help_text="Max 30kg's", max_digits=5),
        ),
        migrations.AddField(
            model_name='quote',
            name='weight4',
            field=models.DecimalField(decimal_places=2, default='0', help_text="Max 30kg's", max_digits=5),
        ),
        migrations.AddField(
            model_name='quote',
            name='width1',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=7),
        ),
        migrations.AddField(
            model_name='quote',
            name='width2',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=7),
        ),
        migrations.AddField(
            model_name='quote',
            name='width3',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=7),
        ),
        migrations.AddField(
            model_name='quote',
            name='width4',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=7),
        ),
        migrations.AlterField(
            model_name='quote',
            name='height',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='quote',
            name='length',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='quote',
            name='volume_weight',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='quote',
            name='width',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
