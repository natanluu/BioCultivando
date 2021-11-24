# Generated by Django 3.2.8 on 2021-11-24 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bioc', '0014_alter_post_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sugestao', models.TextField()),
                ('recado', models.TextField()),
                ('tipo', models.CharField(choices=[('-', '-'), ('SC', 'Suculentas'), ('FT', 'Fitoterápicas')], default='-', max_length=2)),
                ('foto', models.FileField(upload_to='%Y/%m/%d/')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='tipo',
            field=models.CharField(choices=[('-', '-'), ('SC', 'Suculentas'), ('FT', 'Fitoterápicas')], default='-', max_length=2),
        ),
    ]
