# Generated by Django 5.0.3 on 2024-03-19 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='special_room',
        ),
        migrations.AddField(
            model_name='room',
            name='archive_room',
            field=models.BooleanField(default=False, verbose_name='Arquivos'),
        ),
        migrations.AddField(
            model_name='room',
            name='exam_collection_room',
            field=models.BooleanField(default=False, verbose_name='Sala de Coleta de Exames'),
        ),
    ]