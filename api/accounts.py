from main import app, db
from models.users import User
from models.roles import Role
from flask import Flask, jsonify, abort, request, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import uuid


@app.route('/api/v1/accounts/register', methods=['POST'])
def register():
    data = request.json
    try:
        role = Role.query.filter_by(name='User').first()
        u = User(username=data['username'], 
                uuid=uuid.uuid4().hex,
                email=data['email'],
                name = data['name'],
                role_id = role.id,
                password = generate_password_hash(data['password']),
                )
        db.session.add(u)
        ok = db.session.commit()
    except AssertionError as err:
        db.session.rollback()
        abort(409, err) 
    except Exception as err:
        db.session.rollback()
        abort(500, err) 
    finally: 
        db.session.close()
    return make_response(jsonify({'status':'ok','status_code':201}), 201)
    

@app.route('/api/v1/profile/<uuid>', methods=['GET'])
def profile(uuid):
    u = User.query.filter_by(uuid=uuid).first()
    if not u:
        return make_response(jsonify(status='failed',
                                status_code=404, 
                                data={'error':'user not found'}),
                                404)
    return make_response(jsonify(status='ok',
                                status_code=200, 
                                data={'username':u.username,'email':u.email}), 
                                200)

@app.route('/api/v1/accounts/login', methods=['POST'])
def login():
    data = request.json
    try:
        u = User.query.filter_by(email=data['email']).first()
        if not u:
            return make_response(jsonify(status='failed',
                                status_code=422, 
                                data={'error':'user not found'}),
                                422)

        if not check_password_hash(u.password, data['password']):
            return make_response(jsonify(status='failed',
                                status_code=422, 
                                data={'error':'wrong password'}),
                                422)
    except Exception as err:
       return make_response(jsonify(status='failed',
                                status_code=500, 
                                data={'error':'server error'}),
                                500)
    finally: 
        db.session.close()
    
    return make_response(jsonify(status='ok',
                                status_code=200, 
                                data={'token':'insert jwt token'}),
                                200)