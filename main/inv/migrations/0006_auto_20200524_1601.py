# Generated by Django 3.0.6 on 2020-05-24 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0005_auto_20200524_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='operating_system',
            field=models.CharField(blank=True, choices=[('Windows 10', 'Windows 10'), ('Windows 8', 'Windows 8'), ('Windows XP', 'Windows XP'), ('Linux', 'Linux')], max_length=30, null=True),
        ),
    ]