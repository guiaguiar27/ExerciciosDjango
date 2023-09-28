from django.shortcuts import render  
import requests, time 

def home_view(request): 
    start_time = time.time() 
    data = [] 
    url_list = ['https://swapi.dev/api/people', 'https://swapi.dev/api/starships'] 
    for url in url_list: 
        data.append(requests.get(url).json()) 
    final_time = time.time() - start_time 
    print(time)
    return render(request, 'home.html', {'people':data[0], 'starships':data[1]})
