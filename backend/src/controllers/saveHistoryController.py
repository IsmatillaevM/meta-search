import sqlite3

class saveHistoryClass:
    # saveHistory сохраняет историю, которую пользователь посещал
    @staticmethod
    def saveHistory(link:str, title:str)->str:
        
        conn = sqlite3.connect('./src/data/history.db')
        c = conn.cursor()
        
        c.execute('create table if not exists history (link text , title text)')
        
        c.execute('insert into history (link, title) values (?, ?)', (link, title))
        
        conn.commit()

        conn.close()

    
    @staticmethod
    # getHistory возвращает историю, которую пользователь посещал
    def getHistory()->dict:
        conn = sqlite3.connect('./src/data/history.db')
        c = conn.cursor()

        db=c.execute('select * from history')
        
        
        return  [{

            'link':row[0],

            'title':row[1],
        
        } for row in db]

    # saveSearches сохраняет историю поисков который пользователь искал  
    @staticmethod
    def saveSearches(query:str,answer:dict):
        
        conn = sqlite3.connect('./src/data/history.db')
        c = conn.cursor()
        
        c.execute('create table if not exists searches (engine,query, title, link)')
        
        for engine in answer:
            for item in answer[engine]:
                c.execute('insert into searches (engine, query, title, link) values (?, ?, ?, ?)', (engine, query, item['title'], item['link']))

    
        conn.commit()

        conn.close()

    # getSearches возвращает историю поисков который пользователь искал
    @staticmethod
    def getSearches()->dict:
        conn = sqlite3.connect('./src/data/history.db')
        c = conn.cursor()

        db=c.execute('select * from searches')
    
        
        return  [{

            'engine':row[0],

            'query':row[1],

            'title':row[2],

            'link':row[3],
        
        } for row in db]

        