# Generated by Django 2.1 on 2019-05-17 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_auto_20190517_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='last_message',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.TimeField(default='22:15', verbose_name='Time'),
        ),
    ]