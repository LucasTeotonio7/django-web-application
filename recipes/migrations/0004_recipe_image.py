# Generated by Django 4.0.5 on 2022-07-29 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipe_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/%d/%m/%Y/'),
        ),
    ]
