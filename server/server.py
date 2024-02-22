from flask import Flask, jsonify,request
from flask_cors import CORS
from ndtv import scrape_ndtv_data
from et import scrape_et_data
from toi import scrape_toi_data
import feedparser
import threading

app = Flask(__name__)
CORS(app)

@app.route('/search',methods=['POST'])
def search():
    global news_title
    global results
    search_query = request.json.get('query')
    print(search_query)

    results = {}

    def scrape_and_store(scrape_function, key):
        results[key] = scrape_function(search_query)

    ndtv_process = threading.Thread(target=scrape_and_store, args=(scrape_ndtv_data, 'ndtv'))
    toi_process = threading.Thread(target=scrape_and_store, args=(scrape_toi_data, 'toi'))
    et_process = threading.Thread(target=scrape_and_store, args=(scrape_et_data, 'et'))
    
    ndtv_process.start()
    toi_process.start()
    et_process.start()

    ndtv_process.join()
    toi_process.join()
    et_process.join()

    news_title = []

    
    # b = search_query.replace(" ","%20")
    # url = f'https://news.google.com/rss/search?q={b}&hl=en-IN&gl=IN&ceid=IN:en'
    # feed = feedparser.parse(url)
    # for entry in feed.entries:
    #     news_title.append(entry.title)
      
    

    
    for headlines in results.values():
        news_title.extend(headlines)
   

    

    return jsonify({'news_title':news_title})

 
@app.route('/api/data')
def get_data():

    return jsonify({'results':results})



if __name__ == '__main__':
    app.run(debug=True)