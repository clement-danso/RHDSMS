# Generated by Django 2.1 on 2021-01-20 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsapp', '0011_auto_20210119_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='groupID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
