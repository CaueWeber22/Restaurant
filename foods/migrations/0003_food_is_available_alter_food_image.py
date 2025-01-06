# Generated by Django 5.1.4 on 2024-12-27 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_category_food_description_alter_food_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ImageField(default='no_image', upload_to='food_image'),
        ),
    ]