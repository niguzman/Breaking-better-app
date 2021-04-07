from django.shortcuts import render
from django.http import HttpResponse
import requests


def index(request):
    response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes').json()
    breaking = []
    better = []
    for i in response:
        if i['series'] == 'Breaking Bad':
            if int(i['season']) not in breaking:
                breaking.append(int(i['season']))
        else:
            if int(i['season']) not in better:
                better.append(int(i['season']))
    breaking.sort()
    better.sort()
    return render(request, 'myapp/index.html', {'breaking':breaking, 'better':better})

def breakingBad(request, season):
    response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad').json()
    episodes = []
    for i in response:
        if i['season'] == str(season):
            episodes.append(i)
    return render(request, 'myapp/episodes.html', {'episodes': episodes, 'name': 'Breaking Bad', 'number':season})

def betterCallSaul(request, season):
    response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul').json()
    episodes = []
    for i in response:
        if i['season'] == str(season):
            episodes.append(i)
    return render(request, 'myapp/episodes.html', {'episodes': episodes, 'name': 'Better Call Saul', 'number':season})

def detailsEpisode (request, episode_id):
    response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes/'+ str(episode_id)).json()
    info = {}
    for i in response:
        for j in i.keys():
            if j == 'air_date':
                if i[j][5:7] == "01":
                    info[j] = i[j][8:10] + ' de ' + 'enero' + ', ' + i[j][0:4]
                if i[j][5:7] == "02":
                    info[j] = i[j][8:10] + ' de ' + 'febrero' + ', ' + i[j][0:4]
                if i[j][5:7] == "03":
                    info[j] = i[j][8:10] + ' de ' + 'marzo' + ', ' + i[j][0:4]
                if i[j][5:7] == "04":
                    info[j] = i[j][8:10] + ' de ' + 'abril' + ', ' + i[j][0:4]
                if i[j][5:7] == "05":
                    info[j] = i[j][8:10] + ' de ' + 'mayo' + ', ' + i[j][0:4]
                if i[j][5:7] == "06":
                    info[j] = i[j][8:10] + ' de ' + 'junio' + ', ' + i[j][0:4]
                if i[j][5:7] == "07":
                    info[j] = i[j][8:10] + ' de ' + 'julio' + ', ' + i[j][0:4]
                if i[j][5:7] == "08":
                    info[j] = i[j][8:10] + ' de ' + 'agosto' + ', ' + i[j][0:4]
                if i[j][5:7] == "09":
                    info[j] = i[j][8:10] + ' de ' + 'septiembre' + ', ' + i[j][0:4]
                if i[j][5:7] == "10":
                    info[j] = i[j][8:10] + ' de ' + 'octubre' + ', ' + i[j][0:4]
                if i[j][5:7] == "11":
                    info[j] = i[j][8:10] + ' de ' + 'noviembre' + ', ' + i[j][0:4]
                if i[j][5:7] == "12":
                    info[j] = i[j][8:10] + ' de ' + 'diciembre' + ', ' + i[j][0:4]
            else:
                info[j] = i[j]
    return render(request, 'myapp/episode.html', info)

def character(request, name):
    response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/characters?name='+ name.replace(" ", "+")).json()
    quotes = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/quote?author='+ name.replace(" ", "+")).json()
    info = {}
    for i in response:
        for j in i.keys():
            info[j] = i[j]
    return render(request, 'myapp/character.html', {'info': info, 'quotes': quotes})

def search(request):
    srch = request.GET['charac']
    i = 0
    response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/characters?name='+srch+'&offset='+str(i)).json()
    all_characters = []
    while response:
        for j in response:
            all_characters.append(j)
        i+=10
        response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/characters?name='+srch+'&offset='+str(i)).json()


    return render(request, 'myapp/search.html', {'match': all_characters})