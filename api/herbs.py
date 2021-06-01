from main import app, db
from models.herb_list import HerbList
from werkzeug.exceptions import HTTPException
from flask import Flask, jsonify, abort, request, make_response
from sqlalchemy.orm import load_only
from sqlalchemy import or_
from math import ceil


@app.route('/api/v1/herbs', methods=['GET'])
def herbs():
    """Show all data herbs on database
       use parameter /api/v1/herbs?page=<int>&limit=<int> to limit data
    """

    cols = ['uuid', 'name', 'description', 'efficacy', 'recipt', 'image', 'created_at']
    if request.args.get('page'):
        
        if not request.args.get('limit'):
            limit = 5
        else:
            limit = int(request.args.get('limit'))        
        
        page = int(request.args.get('page'))
        herbs = HerbList.query.paginate(page,limit,error_out=False).items
        total_page =  ceil(HerbList.query.count()/limit)
        result = [{col: getattr(d, col) for col in cols} for d in herbs]

        response = {
            'status': 'ok',
            'status_code': 200,
            'data': result,
            'limit': limit,
            'page': page,
            'total_page': total_page,
        }
    else:
        herbs = HerbList.query.all()
        result = [{col: getattr(d, col) for col in cols} for d in herbs]

        response = {
            'status': 'ok',
            'status_code': 200,
            'data': result,
        }

    return make_response(jsonify(response), 200)

@app.route('/api/v1/herb/<uuid>', methods=['GET'])
def herb_detail(uuid):
    """ Show one of herb data using unique uuid """
    if not uuid:
        response = {
            'status': 'failed',
            'status_code': 404,
            'data': {
                'error': 'uuid not found'
            },
        }
        return make_response(jsonify(response), 404)
    else:
        cols = ['uuid', 'name', 'description', 'efficacy', 'recipt', 'image', 'created_at']
        herb = HerbList.query.filter_by(uuid=uuid).options(load_only(*cols)).first()
        
        if not herb:
            response = {
                'status': 'failed',
                'status_code': 404,
                'data': {
                    'error': 'invalid uuid'
                },
            }
            return make_response(jsonify(response), 404)
        else:
            response = {
                'status': 'ok',
                'status_code': 200,
                'data': herb.serialize,
            }
            return make_response(jsonify(response), 200)

@app.route('/api/v1/search-herb', methods=['GET'])
def search_herb():
    """ Search herb data using keyword """
    if not request.args.get('keyword'):
        response = {
            'status': 'failed',
            'status_code': 404,
            'data': {
                'error': 'please input the keywords'
            },
        }
    else:
        keyword = str(request.args.get('keyword'))
        cols = ['uuid', 'name', 'description', 'efficacy', 'recipt', 'image', 'created_at']

        if not request.args.get('limit'):
            limit = 5
        else:
            limit = int(request.args.get('limit'))   

        if not request.args.get('page'):
            page = 1
        else:    
            page =  int(request.args.get('page'))

        herb_is_like = HerbList.query.filter(or_(HerbList.name.ilike('%%%s%%' % keyword), 
                                                HerbList.description.ilike('%%%s%%' % keyword),
                                                HerbList.tags.ilike('%%%s%%' % keyword)))
        herb_item = herb_is_like.paginate(page,limit,error_out=False).items
        total_page =  ceil(herb_is_like.count()/limit)
        result = [{col: getattr(d, col) for col in cols} for d in herb_item]
        
        response = {
            'status': 'ok',
            'status_code': 200,
            'data': result,
            'limit': limit,
            'page': page,
            'total_page': total_page,
        }

        return make_response(jsonify(response), 200)

@app.route('/api/v1/favorite-herb/<uuid>', methods=['PUT'])
def favorite_herb():
    """  Favorited the herb """
    pass

@app.route('/api/v1/my-favorite-herb', methods=['GET'])
def my_favorite_herb():
    """  List of my favorite herb """
    pass


