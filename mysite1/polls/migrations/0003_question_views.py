# Generated by Django 2.2.4 on 2020-03-25 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_question_text_long'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
