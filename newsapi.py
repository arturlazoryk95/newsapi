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
    
    def everything(self, query, pageSize=None, page=None, searchIn=None, sources=None, domains=None, excludeDomains=None, _from=None, _to=None, language=None, sortBy=None):
        
        self.url += 'everything'
    
        params = {

            # Setting up the params
            'q':query,
            'pageSize':pageSize,
            'page':page,
            'searchIn':searchIn,
            'sources': sources,
            'domains': domains,
            'excludeDomains': excludeDomains,
            'from': _from, # 2024-09-29 format
            'to': _to, # 2024-09-29 format
            'language': language, # ar de en es fr he it nl no pt ru sv ud zh
            
            'sortBy': sortBy, 
            # The order to sort the articles in. Possible options: relevancy, popularity, publishedAt.
            #     relevancy = articles more closely related to q come first.
            #     popularity = articles from popular sources and publishers come first.
            #     publishedAt = newest articles come first.

            #     Default: publishedAt
            
            #API KEY added
            'api_key':self.api_key
        }

        notNone_params = {}
        for key, value in params.items():
            if value is not None:
                notNone_params[key]=value
        
        
        response = requests.get(self.url, headers=self.headers, params=notNone_params)
        print(f'Requested URL: {response.url}')
        
        if response.status_code == 200:
            try:
                data = response.json()
                return data
            except json.JSONDecodeError:
                print('Response is not in the JSON format. ')
        else:
            print(f'Received status code: {response.status_code}')
    
    def top_headlines(self, query, pageSize=None, page=None, country=None, category=None, sources=None):
        
        self.url += 'top-headlines'
    
        params = {

            # Setting up the params
            'q':query,
            'pageSize':pageSize,
            'page':page,
            'country':country, # only us option; cannot mix with sources param
            'category': category, # business entertainment general health science sports technology; cannot mix with sources param
            'sources': sources,
            
            # API KEY added
            'api_key':self.api_key
        }

        notNone_params = {}
        for key, value in params.items():
            if value is not None:
                notNone_params[key]=value
        
        
        response = requests.get(self.url, headers=self.headers, params=notNone_params)
        print(f'Requested URL: {response.url}')
        
        if response.status_code == 200:
            try:
                data = response.json()
                return data
            except json.JSONDecodeError:
                print('Response is not in the JSON format. ')
        else:
            print(f'Received status code: {response.status_code}')

    def top_headlines_sources(self, country=None, category=None, language=None):
        
        self.url += 'top-headlines/sources'
    
        params = {

            # Setting up the params
            
            'country':country, 
            # ae ar at au be bg br ca ch cn 
            # co cu cz de eg fr gb gr hk hu 
            # id ie il in it jp kr lt lv ma  
            # mx my ng nl no nz ph pl pt ro 
            # rs ru sa se sg si sk th tr tw ua us ve za
            
            
            'category': category, # business entertainment general health science sports technology; cannot mix with sources param
            'language': language,
            
            # API KEY added
            'api_key':self.api_key
        }

        notNone_params = {}
        for key, value in params.items():
            if value is not None:
                notNone_params[key]=value
        
        
        response = requests.get(self.url, headers=self.headers, params=notNone_params)
        print(f'Requested URL: {response.url}')

        if response.status_code == 200:
            try:
                data = response.json()
                return data
            except json.JSONDecodeError:
                print('Response is not in the JSON format. ')
        else:
            print(f'Received status code: {response.status_code}')