# Generated by Django 5.0.11 on 2025-02-02 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('subscriptions', '0002_alter_subscriptions_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptions',
            name='groups',
            field=models.ManyToManyField(to='auth.group'),
        ),
        migrations.AddField(
            model_name='subscriptions',
            name='premission',
            field=models.ManyToManyField(to='auth.permission'),
        ),
    ]
