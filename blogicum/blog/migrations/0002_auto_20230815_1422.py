# Generated by Django 3.2.16 on 2023-08-15 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
