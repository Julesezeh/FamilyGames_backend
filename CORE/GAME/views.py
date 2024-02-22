from django.shortcuts import render
from .serializers import GameSerializer
from .models import Game
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class GameViews(APIView):
    def get(self,request):
        all_games = Game.objects.all() 
        return Response(all_games)