from django.shortcuts import render  
import requests, time, aiohttp, asyncio   
from .utils import fetch
async def home_view(request): 
    start_time = time.time() 
    url_list = ['http://swapi.dev/api/people','https://swapi.dev/api/starship'] 
    async with aiohttp.ClientSession() as Client: 
        tasks = [] 
        for url in url_list: 
            task = asyncio.ensure_future(fetch(Client,url)) 
            tasks.append(task) 
        results =  await asyncio.gather(*tasks) 
    final_time = time.time() - start_time 
    print(final_time) 
    return render(request, 'home.html', {'people':results[0], 'starship':results[1]})
'''
def home_view(request): 
    start_time = time.time() 
    data = [] 
    url_list = ['https://swapi.dev/api/people', 'https://swapi.dev/api/starships'] 
    for url in url_list: 
        data.append(requests.get(url).json()) 
    final_time = time.time() - start_time 
    print(final_time)
    return render(request, 'home.html', {'people':data[0], 'starships':data[1]}) 
    '''
