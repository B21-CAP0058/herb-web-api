from main import app, db
from models.herb_list import HerbList
from flask import Flask, jsonify, abort, request, make_response
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