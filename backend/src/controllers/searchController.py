from serpapi import GoogleSearch

from serpapi import YandexSearch

from serpapi import BingSearch

import requests

from bs4 import BeautifulSoup


from src.controllers.relevanceFaiss import relevanceClass

  

   
    
 


class searchClass:
#  Функция search возвращает результаты поиска по запросу query, 
    @staticmethod
    def search(query:str) -> dict:
        #  params - параметры поиска в поисковых системах
        params={
        
        'q': {query},
         
         'serp_api_key': 'cc45b19eeb81e95c0e680af7239bc5fa88e5a42276e94badb46fa6d7098d7ab2'
         
         }
        #  paramsvideo - параметры поиска в ютубе. 
        paramsvideo = {
        
        'engine': 'youtube',
        
        'search_query': {query},
        
        'api_key': 'cc45b19eeb81e95c0e680af7239bc5fa88e5a42276e94badb46fa6d7098d7ab2'

        }
    
        # items - словарь с результатами поиска по запросу query в каждой из поисковых систем, который извлекает  органические результаты поиска
        items = {

            'google' : GoogleSearch(params).get_dict()['organic_results'][:1],
            
            'yandex': YandexSearch(params).get_dict()['organic_results'][:1],
            
            'bing': BingSearch(params).get_dict()['organic_results'][:1],

            'youtube' :GoogleSearch(paramsvideo).get_dict()['video_results'][:1]

        }
       
        # return - запускает функцию collectItems
        return  {

            'google': searchClass.collectItems(items['google'],query),

            'yandex': searchClass.collectItems(items['yandex'],query),

            'bing': searchClass.collectItems(items['bing'],query),

            'youtube': items['youtube']

        }

        
    #  Функция collectItems возвращает список словарей с результатами title, link, snippet, relevant поиска по запросу query
    #  relevant - релевантность результатов поиска по запросу query, которая вычисляется с помощью функции relevance из relevanceFaiss.py
    @staticmethod
    def collectItems(items: list,query:str) -> list:
            
            answer = [{
    
                'title': item['title'],
    
                'link': item['link'],
                
                'snippet':item['snippet'],

                'relevant':relevanceClass.relevance(query,searchClass.scrape(item['link'])),

                'query':query 
    
            } for item in items]

            return searchClass.sortbyRelevance(answer)

    #  Функция sortbyRelevance возвращает список словарей упорядоченных по релевантности результатов поиска по запросу query
    @staticmethod
    def sortbyRelevance(items: list) -> list:
        return sorted(items, key=lambda item: item['relevant'], reverse=False)        
    
    #  Функция scrape возвращает текстовое содержимое страницы по ссылке link, 
    @staticmethod
    def scrape(link:str)->list:
        sentences=[]
        try:
            reqs = requests.get(link)

            soup = BeautifulSoup(reqs.text,'html.parser')

            for heading in soup.find_all([ 'p']):
                if len(sentences)<10:
                    if heading.text.replace('\n', ' ')!='':
                        sentences.append(heading.text.replace('\n', ' '))
        except requests.exceptions.ConnectionError:
                sentences.append('not craw')

        if len(sentences)==0:
            sentences.append('not craw')
        
       
        return ' '.join(sentences)
    




       

                
    
            


    




