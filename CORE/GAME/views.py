from django.shortcuts import render, get_object_or_404
from .serializers import GameSerializer, GameCategorySerializer
from .models import Game, GameCategory
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class GameViews(APIView):
    def get(self,request, pk=None):
        if pk is not None:
            game = get_object_or_404(Game,pk=pk)
            print("GAME '': ", game)
            game_serializer = GameSerializer(game,many=False)
            return Response(game_serializer.data)
        
        all_games = Game.objects.all() 
        game_serializer = GameSerializer(all_games,many=True)
        return Response(game_serializer.data)


class CategoryViews(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            selected_category = get_object_or_404(GameCategory,pk=pk)
            if selected_category:
                games = selected_category.game
                serialized_games = GameSerializer(games)
                return Response(serialized_games.data)
        categories_qs = GameCategory.objects.all()
        categories = GameCategorySerializer(categories_qs,many=True)
        return Response(categories.data)