from django.shortcuts import render
from .models import Pokemon, Type

import requests

# 00. Función utilizado en 'inicio.html'
def inicio(request):
    return render(request, 'consultas_app/inicio.html')

# 01. Función utilizada en 'lista_50_pokemons.html'
def lista_50_pokemons(request):
    url      = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(url)
    data     = response.json()['results'][:50]

    print(len(data)) # Observación: La lista brinda como resultado 20 pokemones

    # Obtener información de cada Pokemon
    pokemon_info = []
    for result in data:
        pokemon_url    = result['url']
        pokemon_json = requests.get(pokemon_url).json()

        # Extraer información solicitada
        pokemon_data = {
            'id': pokemon_json['id'],
            'nombre': pokemon_json['name'],
            'tipo': [tipo['type']['name'] for tipo in pokemon_json['types']],
            'altura': pokemon_json['height'],
            'peso': pokemon_json['weight'],
        }

        pokemon_info.append(pokemon_data)
    
    # Visualizar información
    context  = {'pokemon_list': pokemon_info}
    return render(request, 'consultas_app/lista_50_pokemons.html', context)

# 02. Función utilizada en 'rango_peso.html'
def pokemon_rango_peso(request):

    # Obtener todos los pokemones del API
    url = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(url)
    data = response.json()['results']

    # Filtrar los pokemones por peso: [30 - 80]
    lista_rango_peso = []
    for result in data:
        pokemon_url = result['url']
        pokemon_json = requests.get(pokemon_url).json()

        peso = pokemon_json['weight']
        if 30 <= peso <= 80:
            pokemon_data = {
                'id': pokemon_json['id'],
                'nombre': pokemon_json['name'],
                'tipo': [tipo['type']['name'] for tipo in pokemon_json['types']],
                'altura': pokemon_json['height'],
                'peso': peso,
            }
            lista_rango_peso.append(pokemon_data)

    # Prueba: visualizar N° de resultados de la lista en consola
    print(len(lista_rango_peso))

    # Visualizar rango de peso filtrado
    context_peso = {'lista_rango_peso': lista_rango_peso}
    return render(request, 'consultas_app/rango_peso.html', context_peso)

# 04. Función utilizada en 'tipo_grass.html'
def pokemon_tipo_grass(request):

    # Obtener todos los pokemones del API
    url = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(url)
    data = response.json()['results']

    # Filtrar por tipo flying y altura > 10
    lista_tipo_grass = []
    for result in data:
        pokemon_url  = result['url']
        pokemon_json = requests.get(pokemon_url).json()

        # Definir variables cuyas condiciones se deben cumplir
        tipos_pokemon = [tipo['type']['name'] for tipo in pokemon_json['types']]

        # Indicar condiciones
        if 'grass' in tipos_pokemon:
            pokemon_data = {
                'id': pokemon_json['id'],
                'nombre': pokemon_json['name'],
                'tipo': tipos_pokemon,
                'altura': pokemon_json['height'],
                'peso': pokemon_json['weight'],
            }
            lista_tipo_grass.append(pokemon_data)

            # Prueba: visualizar N° de resultados de la lista en consola
    print(len(lista_tipo_grass))

    # Visualizar rango de peso filtrado
    context_tipo_grass = {'lista_tipo_grass': lista_tipo_grass}
    return render(request, 'consultas_app/tipo_grass.html', context_tipo_grass)

# 04. Función utilizada en 'tipo_flying.html'
def pokemon_tipo_flying(request):

    # Obtener todos los pokemones del API
    url = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(url)
    data = response.json()['results']

    # Filtrar por tipo flying y altura > 10
    lista_tipo_flying = []
    for result in data:
        pokemon_url  = result['url']
        pokemon_json = requests.get(pokemon_url).json()

        # Definir variables cuyas condiciones se deben cumplir
        tipos_pokemon = [tipo['type']['name'] for tipo in pokemon_json['types']]
        altura = pokemon_json['height']

        # Indicar condiciones
        if 'flying' in tipos_pokemon and altura >= 10:
            pokemon_data = {
                'id': pokemon_json['id'],
                'nombre': pokemon_json['name'],
                'tipo': tipos_pokemon,
                'altura': altura,
                'peso': pokemon_json['weight'],
            }
            lista_tipo_flying.append(pokemon_data)

            # Prueba: visualizar N° de resultados de la lista en consola
    print(len(lista_tipo_flying))

    # Visualizar rango de peso filtrado
    context_tipo = {'lista_tipo_flying': lista_tipo_flying}
    return render(request, 'consultas_app/tipo_flying.html', context_tipo)

# 05. Función utilizada en 'nombres_invertidos.html'
def nombres_invertidos(request):

    # Obtener todos los pokemones del API
    url = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(url)
    data = response.json()['results']

    # Invertir los nombres de los pokemones
    lista_nombres_invertidos = []
    for result in data:
        pokemon_url  = result['url']
        pokemon_json = requests.get(pokemon_url).json()

        # Invertir el nombre
        nombre           = pokemon_json['name']
        nombre_invertido = nombre[::-1]

        # Construir el objeto con la información requerida
        pokemon_data = {
            'id': pokemon_json['id'],
            'nombre': nombre,
            'nombre_invertido': nombre_invertido,
            'tipo': [tipo['type']['name'] for tipo in pokemon_json['types']],
            'altura': pokemon_json['height'],
            'peso': pokemon_json['weight'],
        }
        lista_nombres_invertidos.append(pokemon_data)

        # Prueba: visualizar N° de resultados de la lista en consola
        print(len(lista_nombres_invertidos))

    # Visualizar lista de nombres invertidos
    context_nombres = {'lista_nombres_invertidos': lista_nombres_invertidos}
    return render(request, 'consultas_app/nombres_invertidos.html', context_nombres)



