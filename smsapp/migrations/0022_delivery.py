# Generated by Django 2.1 on 2021-01-21 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsapp', '0021_delete_delivery'),
    ]

    operations = [
        migrations.CreateModel(
            name='delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sms_status', models.CharField(max_length=50)),
                ('smstype', models.CharField(max_length=50)),
                ('total_sent', models.CharField(max_length=50)),
                ('total_rejected', models.CharField(max_length=50)),
                ('recipient', models.CharField(max_length=50)),
                ('credit_used', models.CharField(max_length=50)),
                ('credit_left', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Deliveries',
            },
        ),
    ]
