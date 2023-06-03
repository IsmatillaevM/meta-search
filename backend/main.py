# Bismillah



from flask import Flask , request

from flask_cors import CORS



import json

import requests

from src.controllers.searchController import searchClass

from src.controllers.saveHistoryController import saveHistoryClass

from src.controllers.offlineCotroller import offlineClass



app = Flask(__name__)
CORS(app)








# этот метод возвращает результаты поиска json формате по запросу и сохраняет историю поиска в базу данных.
# он запускает контроллер  searchClass.search( ) который возвращает результаты поиска и 
# контроллер saveHistoryClass.saveSearches( ) который сохраняет историю поиска в базу данных

@app.route('/search',methods=['GET', 'POST'])
def search():

        query=json.loads(request.data)

        answer=searchClass.search(query['search'])
        
        saveHistoryClass.saveSearches(query['search'],answer)

        return json.dumps(answer) 



# этот метод возвращает историю поиска
# он запускает контроллер  saveHistoryClass.getHistory( ) который возвращает историю поиска
@app.route('/getSearches',methods=['GET', 'POST'])
def getSearches():
        
        return json.dumps(saveHistoryClass.getSearches())




# этот метод сохраняет историю поиска
# он запускает контроллер  saveHistoryClass.saveHistory( ) который сохраняет историю поиска
@app.route('/saveHistory',methods=['GET', 'POST'])
def saveHistory():

        query=json.loads(request.data)
        
        return json.dumps(saveHistoryClass.saveHistory(query["link"],query["title"])) 


# этот метод возвращает историю использованных ответов поисковых систем
# он запускает контроллер  saveHistoryClass.getAnswers( ) который возвращает историю использованных ответов поисковых систем
@app.route('/getHistory',methods=['GET', 'POST'])
def getHistory():

        
        return json.dumps(saveHistoryClass.getHistory()) 


# этот метод возвращает ответов поиска по запросу
# он запускает контроллер  saveHistoryClass.getAnswers( ) который возвращает ответов поиска по запросу
@app.route('/getAnswers',methods=['GET', 'POST'])
def getAnswers():

        
        return json.dumps(saveHistoryClass.getSearches())




@app.route('/addoffline',methods=['GET', 'POST'])
def addoffline():
        title=json.loads(request.data)['title']
        
        link=json.loads(request.data)['link']

        query=json.loads(request.data)['query']

        
        offlineClass.addOffline(title,link,query)
        
        
        return json.dumps('ok')


@app.route('/getoffline',methods=['GET', 'POST'])
def getoffline():

        return json.dumps(offlineClass.getoffline())


if __name__ =='__main__':
        app.run()