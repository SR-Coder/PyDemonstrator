# Generated by Django 2.2.4 on 2021-01-27 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gateway', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='accessLevel',
            field=models.IntegerField(max_length=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.DateField(null=True),
        ),
    ]
