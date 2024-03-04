# Generated by Django 5.0.1 on 2024-03-04 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=1000)),
                ('party1_id', models.CharField(max_length=100)),
                ('party1_name', models.CharField(max_length=100)),
                ('party2_id', models.CharField(default='x', max_length=100)),
                ('party2_name', models.CharField(default='x', max_length=100)),
                ('other_parties', models.TextField(default='[]')),
                ('bid_category', models.CharField(max_length=100, null=True)),
                ('bid_sub_category', models.CharField(max_length=100, null=True)),
                ('bid_type', models.CharField(max_length=10, null=True)),
                ('bid_win_type', models.CharField(max_length=10, null=True)),
                ('bid_status', models.CharField(max_length=20, null=True)),
                ('bid_opening_time', models.TextField(null=True)),
                ('bid_closing_time', models.TextField(null=True)),
                ('is_approved', models.CharField(default='no', max_length=5)),
                ('bid_quantity', models.CharField(max_length=20, null=True)),
                ('bid_delivery_time', models.CharField(max_length=20, null=True)),
                ('bid_material', models.CharField(max_length=20, null=True)),
                ('percentage_inc_dec', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Domains',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemsCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemsSubCategories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_category', models.CharField(max_length=200, null=True)),
                ('category_id', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('user_id', models.CharField(blank=True, max_length=10, null=True)),
                ('item_type', models.CharField(blank=True, max_length=100, null=True)),
                ('item_price', models.CharField(blank=True, max_length=100, null=True)),
                ('item_availability', models.CharField(blank=True, max_length=100, null=True)),
                ('item_category', models.CharField(blank=True, max_length=100, null=True)),
                ('item_sub_category', models.CharField(blank=True, max_length=100, null=True)),
                ('img', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('party1_id', models.CharField(max_length=100)),
                ('party1_name', models.CharField(max_length=100)),
                ('party2_id', models.CharField(max_length=100)),
                ('party2_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Refers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('manufacturer_id', models.CharField(max_length=200, null=True)),
                ('manufacturer_username', models.CharField(max_length=200, null=True)),
                ('seller_id', models.CharField(max_length=200, null=True)),
                ('seller_username', models.CharField(max_length=200, null=True)),
                ('referral_price', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scraps',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('user_id', models.CharField(max_length=10)),
                ('item_type', models.CharField(max_length=100)),
                ('item_price', models.CharField(max_length=100)),
                ('item_quantity', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('user_id', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200, null=True, unique=True)),
                ('email', models.CharField(max_length=200, null=True, unique=True)),
                ('phone', models.CharField(max_length=200, null=True, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('user_type', models.CharField(max_length=200)),
                ('user_types', models.JSONField(default=list)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('company_name', models.CharField(blank=True, max_length=500, null=True)),
                ('company_size', models.CharField(blank=True, max_length=500, null=True)),
                ('manufacturer_category', models.CharField(blank=True, max_length=500, null=True)),
                ('adhaar_number', models.CharField(blank=True, max_length=200, null=True)),
                ('is_approved', models.CharField(blank=True, default='no', max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
