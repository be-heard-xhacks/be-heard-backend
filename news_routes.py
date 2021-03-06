from bson.objectid import ObjectId
from route_config import *
from flask import jsonify, make_response, request
import requests
import os
import json
from auth_routes import auth_required
  
@app.route("/getArticles", methods = ["GET"])
@auth_required
def getArticles(uid):
    objID = ObjectId(uid)
    if not objID:
        return make_response(jsonify({'message' : 'missing uid'}), 404)
    # request_data = request.args
    # if request.is_json:
    #     request_data = request.get_json()
    request_queries = db.users.find_one({"_id": objID})['interests']
    parsed_articles = []
    for request_query in request_queries:
        payload_params = {
            'q': request_query, 
            'pageNumber' : '1', 
            'pageSize': '5', 
            'autoCorrect': 'true',
            'fromPublishedDate': 'null',
            'toPublishedDate': 'null',
            'withThumbnails' : 'true'
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

        for article in api_response_articles:
            article_info = {}
            article_info['title'] = article['title']
            article_info['link'] = article['url']
            article_info['summary'] = article['description']
            article_info['time'] = article['datePublished']
            article_info['id'] = article['id']
            article_info['interest'] = request_query
            article_images = article['image']
            if article_images:
                article_info['img'] = article_images['thumbnail']
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
            parsed_articles.append(article_info)
            
        

    return jsonify({"data" : parsed_articles })

@app.route("/getTrending", methods=["GET"])
@auth_required
def getTrending(uid):
    objID = ObjectId(uid)
    if not objID:
        return make_response(jsonify({'message' : 'missing uid'}), 404)
    
    payload_params = {
        'pageNumber' : '1',
        'pageSize' : '10',
        'withThumbnails': 'true',
        'location' : 'us'
    }

    payload_headers = {
        'x-rapidapi-key' : os.environ.get('X_RAPIDAPI_KEY_1'),
        'x-rapidapi-host' : os.environ.get('X_RAPIDAPI_HOST')
    }

    api_response = requests.get('https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/search/TrendingNewsAPI',
        headers= payload_headers,
        params=payload_params)
    api_response=api_response.text
    api_response_data= json.loads(api_response)
    api_response_articles = api_response_data['value']
    
    parsed_articles = []
    for article in api_response_articles:
        article_info = {}
        article_info['title'] = article['title']
        article_info['link'] = article['url']
        article_info['summary'] = article['description']
        article_info['time'] = article['datePublished']
        article_info['id'] = article['id']
        article_images = article['image']
        if article_images:
            article_info['img'] = article_images['thumbnail']
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
        parsed_articles.append(article_info)

    return jsonify({"data" : parsed_articles })
    
