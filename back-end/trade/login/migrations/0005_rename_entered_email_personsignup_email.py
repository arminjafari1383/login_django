# Generated by Django 4.2.8 on 2024-04-19 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_rename_email_personsignup_entered_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personsignup',
            old_name='entered_email',
            new_name='email',
        ),
    ]
