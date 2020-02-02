# Generated by Django 3.0.2 on 2020-02-02 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='delivery_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='discount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='item',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='mobile',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='paid_amount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='rate',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]