# Generated by Django 3.1.4 on 2021-03-14 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0040_auto_20210311_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='overall_volume',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quote',
            name='overall_weight',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quote',
            name='height1',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='height2',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='height3',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='height4',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='length1',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='length2',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='length3',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='length4',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='volume_weight',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quote',
            name='volume_weight1',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='volume_weight2',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='volume_weight3',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='volume_weight4',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='weight1',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text="Max 30kg's", max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='weight2',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text="Max 30kg's", max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='weight3',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text="Max 30kg's", max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='weight4',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text="Max 30kg's", max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='width1',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='width2',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='width3',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='width4',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]
