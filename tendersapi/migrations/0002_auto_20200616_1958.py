# Generated by Django 3.0.7 on 2020-06-16 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tendersapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bartender',
            name='image_url',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]