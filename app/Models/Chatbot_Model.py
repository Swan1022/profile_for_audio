from app.Database import db

URL_DB = db.urls

def check_already_searched(url):
    result = URL_DB.find_one({"url": url})
    if result != None:
      del result['_id']
    return result
  
def insert_url_database(url, media):
    result = URL_DB.insert_one({"url": url, "media": media})