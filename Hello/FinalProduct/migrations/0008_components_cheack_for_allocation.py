# Generated by Django 2.2.3 on 2019-07-12 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinalProduct', '0007_rawmaterial_flag'),
    ]

    operations = [
        migrations.AddField(
            model_name='components',
            name='Cheack_for_Allocation',
            field=models.BooleanField(default=True),
        ),
    ]
