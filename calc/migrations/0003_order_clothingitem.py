# Generated by Django 2.2.5 on 2020-03-06 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_auto_20200306_0300'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='clothingItem',
            field=models.CharField(default='TSHIRT', max_length=120),
            preserve_default=False,
        ),
    ]