from newsapi import NewsAPIClient
from filemanager import FileManager

if __name__ == '__main__':

    News = NewsAPIClient()
    
    response = News.everything(query='Apple Watch Ultra 2', pageSize=5)

    MyFiles = FileManager('outputs/')
    MyFiles.put_into_json('output2.json', response)