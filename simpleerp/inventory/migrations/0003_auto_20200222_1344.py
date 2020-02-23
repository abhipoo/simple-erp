# Generated by Django 3.0.3 on 2020-02-22 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_inventorychangelog'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='dtp_cost',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='sales',
            name='dtp_page_count',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='sales',
            name='page_type',
            field=models.CharField(default='single', max_length=100),
            preserve_default=False,
        ),
    ]
