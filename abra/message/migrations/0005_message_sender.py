# Generated by Django 4.0.5 on 2022-06-08 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0004_rename_name_message_message_remove_message_paradigm_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='Sender',
            field=models.CharField(default=None, max_length=100),
        ),
    ]