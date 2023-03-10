# Generated by Django 4.1.5 on 2023-01-10 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0011_alter_pages_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pages',
            options={'ordering': ['-fecha']},
        ),
        migrations.RenameField(
            model_name='pages',
            old_name='author',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='pages',
            old_name='content',
            new_name='contenido',
        ),
        migrations.RenameField(
            model_name='pages',
            old_name='status',
            new_name='estado',
        ),
        migrations.RenameField(
            model_name='pages',
            old_name='slug',
            new_name='etiqueta',
        ),
        migrations.RenameField(
            model_name='pages',
            old_name='date',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='pages',
            old_name='image',
            new_name='imagen',
        ),
        migrations.RenameField(
            model_name='pages',
            old_name='subtitle',
            new_name='subtitulo',
        ),
        migrations.RenameField(
            model_name='pages',
            old_name='title',
            new_name='titulo',
        ),
    ]
