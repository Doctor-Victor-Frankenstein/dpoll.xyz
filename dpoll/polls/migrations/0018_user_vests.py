# Generated by Django 2.1.1 on 2019-04-08 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_question_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='vests',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=64, null=True),
        ),
    ]
