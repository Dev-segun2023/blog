# Generated by Django 5.0.3 on 2024-05-15 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='media'),
        ),
    ]
