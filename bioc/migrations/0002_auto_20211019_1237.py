# Generated by Django 3.2.8 on 2021-10-19 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bioc', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bioc',
            new_name='Fito',
        ),
        migrations.CreateModel(
            name='Sucu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bioc.post')),
            ],
        ),
    ]
