from route_config import *
from flask import jsonify, make_response, request
import requests
import os
import json
from auth_routes import auth_required
  
@app.route("/getArticles", methods = ["GET"])
@auth_required
def getArticles():
    request_data = request.args
    if request.is_json:
        request_data = request.get_json()
    request_query = request_data.get('searchTerm')
    payload_params = {
        'q': request_query, 
        'pageNumber' : '1', 
        'pageSize': '10', 
        'autoCorrect': 'true',
        'fromPublishedDate': 'null',
        'toPublishedDate': 'null'
        }
    
    payload_headers = {
        'x-rapidapi-key' : os.environ.get('X_RAPIDAPI_KEY_1'),
        'x-rapidapi-host' : os.environ.get('X_RAPIDAPI_HOST')
    }
    api_response = requests.get('https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/search/NewsSearchAPI',
    headers=payload_headers,
    params=payload_params
    )
    api_response = api_response.text
    api_response_data=json.loads(api_response)
    api_response_articles = api_response_data['value']

    parsed_infos = []
    for article in api_response_articles:
        article_info = {}
        article_info['title'] = article['title']
        article_info['link'] = article['url']
        article_info['summary'] = article['description']
        article_info['time'] = article['datePublished']
        article_images = article['image']
        if article_images:
            article_info['img'] = article_images['url']
        else:
            article_info['img'] = ""
        article_provider_info = article['provider']
        if article_provider_info:
            article_info['source'] = article_provider_info['name']
            source_img = article_provider_info['favIcon']
            if source_img:
                article_info['sourceIcon'] = source_img
            else:
                article_info['sourceIcon'] = ""
        else:
            article_info['source'] = ""
            article_info['sourceIcon'] = ""
        parsed_infos.append(article_info)
        

    print(api_response_data)
    return jsonify({"data" : parsed_infos })