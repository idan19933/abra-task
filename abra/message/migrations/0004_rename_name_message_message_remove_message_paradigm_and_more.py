# Generated by Django 4.0.5 on 2022-06-08 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('message', '0003_rename_language_message_delete_students'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='name',
            new_name='Message',
        ),
        migrations.RemoveField(
            model_name='message',
            name='paradigm',
        ),
        migrations.AddField(
            model_name='message',
            name='Receiver',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
