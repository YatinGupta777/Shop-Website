# Generated by Django 3.0.2 on 2020-02-08 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='delivered',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]