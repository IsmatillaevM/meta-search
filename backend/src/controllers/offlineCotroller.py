from bs4 import BeautifulSoup
import requests
from src.controllers.analysisController import analysisClass
import sqlite3


class offlineClass:

    @staticmethod
    def addOffline(title,link,query):
        

        response = requests.get(link)
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        body = soup.find('body')

        links=soup.find_all('a')

        analysisText=analysisClass.analysisText(body.get_text())

        conn = sqlite3.connect('./src/data/history.db')
        c = conn.cursor()
        
        c.execute('create table if not exists offline (query text ,title text, body text,analysis text, counta number )')
        
        c.execute('insert into offline (query,title,body,analysis,counta ) values (?,?,?,?,?)', (query,title, str(body), str(analysisText),len(links)))
        
        conn.commit()

        conn.close()
        

        return 'ok'
    

    @staticmethod
    def getoffline():
        
        conn = sqlite3.connect('./src/data/history.db')
        c = conn.cursor()

        db=c.execute('select * from offline')
        
        
        return  [{

            'query':row[0],

            'title':row[1],

            'body':row[2],

            'analysis':row[3],

            'counta':row[4],
        
        } for row in db]
