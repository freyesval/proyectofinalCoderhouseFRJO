# Generated by Django 4.1 on 2022-09-28 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0012_remove_profile_image_alter_avatar_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default.png', upload_to='avatar'),
        ),
        migrations.DeleteModel(
            name='Avatar',
        ),
    ]
