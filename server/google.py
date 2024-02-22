import feedparser
# search_query = "budget 2024"
def google_news_scrape(search_query):
    b = search_query.replace(" ","%20")
    url = f'https://news.google.com/rss/search?q={b}&hl=en-IN&gl=IN&ceid=IN:en'
    feed = feedparser.parse(url)
    
    # count = 0
    headline_list = []
    for entry in feed.entries:
        headline_list.append(entry.title)
        # count = count + 1
        # title = entry.title
        # pubdate = entry.published
        # source = entry.source.title
        # print(f"{count}\nTitle: {title}\nPublished_Date: {pubdate}\nSource: {source}\n")
    return headline_list

# query = 'india%20budget%202024'
