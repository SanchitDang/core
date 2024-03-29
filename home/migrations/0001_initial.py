# Generated by Django 5.0.1 on 2024-03-04 09:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PanelUser',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('user_type', models.CharField(blank=True, choices=[('Admin', 'Admin'), ('Execution', 'Execution'), ('Service_support', 'Service support'), ('Freelancers', 'Freelancers')], max_length=20)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Assessments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('supplier_address', models.CharField(blank=True, max_length=100, null=True)),
                ('supplier_location', models.CharField(blank=True, max_length=100, null=True)),
                ('items', models.CharField(blank=True, max_length=100, null=True)),
                ('assessed_mode', models.CharField(blank=True, max_length=1000, null=True)),
                ('assessed_by', models.CharField(blank=True, max_length=100, null=True)),
                ('assessment_date', models.DateField(blank=True, null=True)),
                ('assessment_for', models.CharField(blank=True, choices=[('Scrap', 'Scrap'), ('Raw material', 'Raw material'), ('Services', 'Services')], max_length=100, null=True)),
                ('previous_assessment_date', models.DateField(blank=True, null=True)),
                ('organization_structure_details', models.FileField(blank=True, null=True, upload_to='')),
                ('satuatory_documents_details', models.FileField(blank=True, null=True, upload_to='')),
                ('work_resistration', models.FileField(blank=True, null=True, upload_to='')),
                ('work_address_ownership_lease_document', models.FileField(blank=True, null=True, upload_to='')),
                ('quality_managment_system', models.FileField(blank=True, null=True, upload_to='')),
                ('design_capability', models.FileField(blank=True, null=True, upload_to='')),
                ('manufacturing_facility', models.FileField(blank=True, null=True, upload_to='')),
                ('testing_facility', models.FileField(blank=True, null=True, upload_to='')),
                ('processing_capability', models.FileField(blank=True, null=True, upload_to='')),
                ('supply_experience', models.FileField(blank=True, null=True, upload_to='')),
                ('safety_aspect', models.FileField(blank=True, null=True, upload_to='')),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('established_year', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to='apis.users')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_by', to='apis.users')),
            ],
        ),
    ]
