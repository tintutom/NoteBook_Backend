# Generated by Django 4.1.7 on 2023-06-30 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_note_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='desciption',
            new_name='description',
        ),
    ]