# Generated by Django 3.2.8 on 2021-10-19 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bioc', '0003_auto_20211019_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caract',
            field=models.CharField(default='características da espécie', max_length=300),
        ),
        migrations.AlterField(
            model_name='post',
            name='cores',
            field=models.CharField(default='cores da espécies', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='sobre',
            field=models.CharField(default='sobre a espécie', max_length=300),
        ),
        migrations.AlterField(
            model_name='post',
            name='tamanho',
            field=models.CharField(default='tamanho da espécie', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='texto',
            field=models.CharField(default='nome científico', max_length=50),
        ),
    ]
