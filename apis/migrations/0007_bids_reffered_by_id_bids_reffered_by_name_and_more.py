# Generated by Django 5.0.1 on 2024-03-09 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0006_domains_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='bids',
            name='reffered_by_id',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bids',
            name='reffered_by_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='refers',
            name='reffered_by_id',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='refers',
            name='reffered_by_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
