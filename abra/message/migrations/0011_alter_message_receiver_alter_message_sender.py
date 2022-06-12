# Generated by Django 4.0.5 on 2022-06-11 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0010_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='Receiver',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='message.user'),
        ),
        migrations.AlterField(
            model_name='message',
            name='Sender',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='message.user'),
        ),
    ]