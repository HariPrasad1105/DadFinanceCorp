# Generated by Django 2.0.4 on 2018-05-19 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinanceCorp', '0003_lender_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='payee',
            name='type',
            field=models.CharField(default='payee', max_length=10),
        ),
    ]
