# Generated by Django 5.1.7 on 2025-04-11 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_cuisine_recipe_cuisines'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='cuisines',
            new_name='cuisine',
        ),
    ]
