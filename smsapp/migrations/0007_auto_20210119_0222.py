# Generated by Django 2.1 on 2021-01-19 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smsapp', '0006_auto_20210119_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='broadcastmessage',
            name='Group',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='broadcastmessage',
            name='MessageTemplate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='smsapp.messagetemp'),
        ),
    ]
