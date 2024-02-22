from django.shortcuts import render
from .serializers import GameSerializer
from .models import Game
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class GameViews(APIView):
    def get(self,request, pk=None):
        if pk:
            game = Game.objects.filter(pk=pk)
            game_serializer = GameSerializer(game)
            return Response(game_serializer.data)
        all_games = Game.objects.all() 
        game_serializer = GameSerializer(all_games,many=True)
        return Response(game_serializer.data)