# Generated by Django 5.1.3 on 2025-04-03 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('softdesk_api', '0002_alter_contributor_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contributor',
            options={'ordering': ['id']},
        ),
    ]
