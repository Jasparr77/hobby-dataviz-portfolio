# Generated by Django 2.1.4 on 2018-12-18 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vizzes', '0010_auto_20181217_1350'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MLB_beers',
        ),
        migrations.DeleteModel(
            name='women_congress',
        ),
        migrations.AlterField(
            model_name='dataviz',
            name='viz_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]