# Generated by Django 5.1 on 2024-08-23 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artikel',
            name='bilder',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]