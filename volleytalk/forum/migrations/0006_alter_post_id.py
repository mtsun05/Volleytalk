# Generated by Django 5.0.6 on 2024-06-18 18:27

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b2e43390-a474-4a88-8496-8e687aac350a'), editable=False, primary_key=True, serialize=False),
        ),
    ]
