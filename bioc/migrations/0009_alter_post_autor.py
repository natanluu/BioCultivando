# Generated by Django 3.2.8 on 2021-10-24 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bioc', '0008_alter_post_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='autor',
            field=models.CharField(max_length=30),
        ),
    ]
