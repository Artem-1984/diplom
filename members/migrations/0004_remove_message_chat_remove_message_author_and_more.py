# Generated by Django 5.0.7 on 2024-07-23 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_chat_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='chat',
        ),
        migrations.RemoveField(
            model_name='message',
            name='author',
        ),
        migrations.DeleteModel(
            name='Chat',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
