# Generated by Django 3.2.8 on 2021-10-24 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bioc', '0005_auto_20211019_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tipo',
            field=models.CharField(choices=[('Suculentas', 'Suculentas'), ('Fitoterápicas', 'Fitoterápicas')], default='Suculentas', max_length=50),
        ),
    ]
