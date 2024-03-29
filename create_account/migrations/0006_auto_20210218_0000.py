# Generated by Django 3.1.4 on 2021-02-18 00:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('create_account', '0005_auto_20210216_0053'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='create_account',
            options={'verbose_name': 'account', 'verbose_name_plural': 'Account Submissions'},
        ),
        migrations.AddField(
            model_name='create_account',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='create_account',
            name='phone_number',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='create_account',
            name='complete',
            field=models.BooleanField(default=False, help_text='Only Select Complete Once Account is 100% Set Up!', verbose_name='Complete'),
        ),
    ]
