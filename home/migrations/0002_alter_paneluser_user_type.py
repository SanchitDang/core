# Generated by Django 5.0.1 on 2024-03-05 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paneluser',
            name='user_type',
            field=models.CharField(blank=True, choices=[('Admin', 'Admin'), ('Execution', 'Execution'), ('Service_support', 'Service support'), ('Freelancers', 'Freelancers'), ('referral', 'referral')], max_length=20),
        ),
    ]
