# Generated by Django 2.1.7 on 2019-12-25 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='aliases',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(db_index=True, max_length=255),
        ),
    ]
