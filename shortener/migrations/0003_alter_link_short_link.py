# Generated by Django 4.0.3 on 2022-03-26 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_alter_link_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='short_link',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]