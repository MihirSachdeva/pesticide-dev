# Generated by Django 3.1.1 on 2020-09-06 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pesticide_app', '0004_auto_20200906_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuestatus',
            name='status_text',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_text',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
