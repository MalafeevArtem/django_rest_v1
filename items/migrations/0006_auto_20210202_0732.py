# Generated by Django 3.1.5 on 2021-02-02 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_auto_20210130_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='weight',
            field=models.IntegerField(max_length=2147483647),
        ),
    ]