from django.urls import path
from .views      import inicio
from .views      import lista_50_pokemons
from .views      import pokemon_rango_peso
from .views      import pokemon_tipo_grass
from .views      import pokemon_tipo_flying
from .views      import nombres_invertidos

urlpatterns = [
    path('inicio/', inicio, name = 'inicio'),
    path('lista_50_pokemons/', lista_50_pokemons, name = 'pokemones'),
    path('rango_peso/', pokemon_rango_peso, name = 'rango_peso'),
    path('tipo_grass/', pokemon_tipo_grass, name = 'tipo_grass'),
    path('tipo_flying/', pokemon_tipo_flying, name = 'tipo_flying'),
    path('nombres_invertidos/', nombres_invertidos, name = 'nombres_invertidos'),
    
]