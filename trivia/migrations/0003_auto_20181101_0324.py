# Generated by Django 2.1.2 on 2018-11-01 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0002_auto_20181027_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.TextField(max_length=200),
        ),
    ]