# Generated by Django 3.2.20 on 2023-07-31 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_history'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='history',
            options={'verbose_name': 'History', 'verbose_name_plural': 'Histories'},
        ),
        migrations.AlterField(
            model_name='blog',
            name='image_url',
            field=models.URLField(null=True),
        ),
    ]