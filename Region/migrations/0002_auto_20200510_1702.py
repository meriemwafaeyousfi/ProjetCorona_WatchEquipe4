# Generated by Django 3.0.3 on 2020-05-10 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Region', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statistiqueregion',
            name='refuserSt',
        ),
        migrations.AlterField(
            model_name='statistiqueregion',
            name='validerSt',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Validée'),
        ),
    ]
