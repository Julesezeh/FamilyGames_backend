from django.db import models

# Create your models here.

class GameCategory(models.Model):
    title = models.CharField(max_length=22)

    def __str__(self):
        return self.title


class Game(models.Model):
    name = models.CharField(max_length=400)
    category = models.OneToOneField(GameCategory, on_delete=models.CASCADE)
    number_of_players = models.FloatField()
    equipments = models.TextField()
    difficulty = models.IntegerField()
    # one off duration in minutes
    one_off_duration = models.IntegerField()
    likely_to_play_again = models.BooleanField()
    description = models.TextField()
    beginning_to_play = models.TextField()
    game_play = models.TextField()
    extra_notes_title = models.CharField(max_length=100, blank=True)
    extra_notes_details = models.TextField(blank=True)

    def __str__(self):
        return self.name