# Generated by Django 4.1.1 on 2022-11-24 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('especie', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='especie',
            old_name='esp',
            new_name='idespecie',
        ),
    ]
