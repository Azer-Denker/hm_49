# Generated by Django 2.2 on 2020-08-04 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='summary',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
    ]