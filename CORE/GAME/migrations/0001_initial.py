# Generated by Django 5.0.2 on 2024-02-22 07:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=22)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('number_of_players', models.FloatField()),
                ('equipments', models.TextField()),
                ('difficulty', models.IntegerField()),
                ('one_off_duration', models.IntegerField()),
                ('likely_to_play_again', models.BooleanField()),
                ('description', models.TextField()),
                ('beginning_to_play', models.TextField()),
                ('game_play', models.TextField()),
                ('extra_notes_title', models.CharField(max_length=100)),
                ('extra_notes_details', models.TextField()),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='GAME.gamecategory')),
            ],
        ),
    ]
