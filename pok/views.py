import json
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import render

# Create your views here.
from pok.models import Team, Pokemon


def all_pokemon(request):
    pokemon_objects = Pokemon.objects.all()
    collection = []
    for pokemon in pokemon_objects:
        collection.append({
            'name': pokemon.name,
            'image': pokemon.image,
            'pokedex_id': pokemon.pokedex_id,
            'team': {
                'name': pokemon.team.name,
                'id': pokemon.team.id,
            },
        })

    return HttpResponse(json.dumps(collection), content_type='application/json')


@csrf_exempt
def new_pokemon(request):
    pokemon = []
    if request.method == 'POST':
        data = json.loads(request.body)
        pokemon = Pokemon.objects.create(
            name=data['name'],
            image=data['image'],
            pokedex_id=data['pokedex_id'],
            team=Team.objects.get(id=data['team'])
        )
    if not pokemon:
        response = serializers.serialize('json', [])
    else:
        response = serializers.serialize('json', [pokemon])
    return HttpResponse(response, content_type='application/json')


def pokemon(request):
    return render(request, 'pokemon.html')

@csrf_exempt
def new_team(request):
    team = []
    if request.method == 'POST':
        data = json.loads(request.body)
        # Team.objects.create(name=data['team'])
        team = Team.objects.create(
            name=data['name']
        )
    response = serializers.serialize('json', [team])
    return HttpResponse(response, content_type='application/json')