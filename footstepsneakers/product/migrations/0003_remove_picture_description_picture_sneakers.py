# Generated by Django 5.1.7 on 2025-04-11 20:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='description',
        ),
        migrations.AddField(
            model_name='picture',
            name='sneakers',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='product.sneakers'),
            preserve_default=False,
        ),
    ]
