# Generated by Django 3.2.20 on 2023-07-31 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20230731_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
