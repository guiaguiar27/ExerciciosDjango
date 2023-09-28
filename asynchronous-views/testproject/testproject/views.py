from django.shortcuts immport render  
import requests, time 

def home_view(request): 
    start_time = timer.time() 
    data = [] 
    url_list = ['https://swapi.dev/api/people/1/', 'https://swapi.dev/api/starships/9/'] 
    for url in url_list: 
        data.append(request.get(url).json()) 
    final_time = timer.time() - start_time 
    return render(request, 'home.html', {'people':data[0], 'starships':data[1]})
