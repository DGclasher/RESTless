# Generated by Django 4.1.5 on 2023-02-13 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0004_alter_quotes_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='high_auth',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='quotes',
            name='high_auth_quote',
            field=models.BooleanField(default=False),
        ),
    ]
