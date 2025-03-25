# Generated by Django 5.1.3 on 2025-03-25 19:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Structure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('path', models.CharField(max_length=255)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_structures_category', to='categories.category')),
            ],
            options={
                'verbose_name': 'Structure',
                'verbose_name_plural': 'Structures',
            },
        ),
    ]
