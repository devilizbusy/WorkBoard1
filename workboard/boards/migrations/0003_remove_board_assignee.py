# Generated by Django 5.1.1 on 2024-09-26 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_board_assignee_alter_board_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='assignee',
        ),
    ]
