# Generated by Django 2.2.6 on 2019-12-19 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0015_auto_20191219_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='last_message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chatroom_last_message', to='chat.Message'),
        ),
    ]
