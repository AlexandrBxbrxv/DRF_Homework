# Generated by Django 4.2.2 on 2024-10-25 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_lesson'),
        ('users', '0004_payments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Payments',
            new_name='Payment',
        ),
    ]
