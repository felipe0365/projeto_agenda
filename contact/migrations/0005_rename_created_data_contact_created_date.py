# Generated by Django 4.2.7 on 2023-11-30 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_alter_category_options_contact_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='created_data',
            new_name='created_date',
        ),
    ]
