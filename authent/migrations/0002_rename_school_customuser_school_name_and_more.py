# Generated by Django 5.1.4 on 2024-12-13 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authent', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='school',
            new_name='school_name',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
