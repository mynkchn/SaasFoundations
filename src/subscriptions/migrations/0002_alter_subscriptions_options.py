# Generated by Django 5.0.11 on 2025-02-02 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscriptions',
            options={'permissions': [('advanced', 'Advanced Perm'), ('pro', 'Pro Perm'), ('basic', 'Basic Perm'), ('basic_ai', 'Basic_AI Perm')]},
        ),
    ]
