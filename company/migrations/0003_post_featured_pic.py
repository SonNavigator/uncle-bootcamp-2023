# Generated by Django 3.2 on 2023-01-21 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20230121_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured_pic',
            field=models.ImageField(blank=True, null=True, upload_to='cover/'),
        ),
    ]