# Generated by Django 5.0.1 on 2024-03-07 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0003_alter_bids_bid_closing_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='is_approved',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
