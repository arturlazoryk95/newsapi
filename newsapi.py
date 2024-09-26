import requests
from decouple import config
import json
from filemanager import FileManager


class NewsAPIClient:
    def __init__(self):
        self.api_key = config('NEWS_API_KEY')
        self.headers = {
            'Authorization' : f'Bearer {self.api_key}'
        }
        self.url = 'https://newsapi.org/v2/'
    
    def everything(self, query, pageSize=None, page=None):
        self.url += 'everything?'
    
        self.url += f'q={query}'
        
        if pageSize: 
            self.url += f'&pageSize={pageSize}'
        
        if page:
            self.url += f'&page={page}'

        self.url += f'&{self.api_key}'

        response = requests.get(self.url, headers=self.headers)
        return response.json()
