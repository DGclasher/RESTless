# Generated by Django 4.1.5 on 2023-01-28 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_author_alter_quotes_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='author',
            new_name='name',
        ),
    ]
