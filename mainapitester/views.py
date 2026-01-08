from django.shortcuts import render
from django.http.response import HttpResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response


from mainapitester.mods.ffvi.enemydata import get_data as EnemyData

def simple_view(request):
    return HttpResponse("Simple view")

@api_view(['GET'])
def test_api_call(request):
    return Response("Successful API Call! Hello, world!")

@api_view(['GET'])
def ffvi_bestiary(request, enemy_number):
    if enemy_number <= 0:
        return Response("Not a valid number!")
    elif enemy_number > 384:
        return Response("Not a valid number!")
    else:
        return Response(EnemyData(enemy_number))




