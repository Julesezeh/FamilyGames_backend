# Generated by Django 5.0.2 on 2024-02-22 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GAME', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='extra_notes_details',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='extra_notes_title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]