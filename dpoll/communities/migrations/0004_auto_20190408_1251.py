# Generated by Django 2.1.1 on 2019-04-08 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0003_auto_20190408_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='members',
            field=models.TextField(blank=True, help_text='A list of members separated by newlines. (\\n)', null=True),
        ),
    ]
