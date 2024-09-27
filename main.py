from newsapi import NewsAPIClient
from filemanager import FileManager

if __name__ == '__main__':

    News = NewsAPIClient()
    
    query = "War in Ukraine"
    response = News.everything(query=query, _from='2024-09-26', language='en', sortBy='popularity')

    MyFiles = FileManager('outputs/')
    MyFiles.put_into_json(f'{query}.json', response)