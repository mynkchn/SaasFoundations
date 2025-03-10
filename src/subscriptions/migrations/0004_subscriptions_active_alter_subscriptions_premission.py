# Generated by Django 5.0.11 on 2025-02-07 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('subscriptions', '0003_subscriptions_groups_subscriptions_premission'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptions',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='subscriptions',
            name='premission',
            field=models.ManyToManyField(limit_choices_to={'codename__in': ['advanced', 'pro', 'basic', 'basic_ai'], 'content_type__app_label': 'subscriptions'}, to='auth.permission'),
        ),
    ]
