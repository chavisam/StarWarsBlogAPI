"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os 
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Character, Planet, Starship, Character_favorites , Planet_favorites, User
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = os.environ.get('JWT-SECRET')
jwt = JWTManager(app)








app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# GET ALL CHARACTERS
@app.route('/people', methods=['GET'])
@jwt_required()
def handle_hello():

    character_query = Character.query.all()
    all_characters = list(map(lambda x: x.serialize(), character_query))
    return jsonify(all_characters)

# GET PUT AND DELETE ONE CHARACTER
@app.route('/people/<int:character_id>', methods=['GET' , 'PUT' ,'DELETE'])
def get_one_character(character_id):  

    body = request.get_json() #{ 'character_name': 'new_charactername'}
   
    if request.method == 'PUT':
        character1 = Character.query.get(character_id)

        if character1 is None:
            raise APIException('User not found', status_code=404)

        if "character_name" in body:
            character1.character_name = body["character_name"]
        if "hair_color" in body:
            character1.hair_color = body["hair_color"]
        if "gender" in body:
            character1.hair_color = body["gender"]
        db.session.commit()
        return jsonify(character1.serialize()), 200


    if request.method == 'GET':
        character_query = Character.query.get(character_id)
        return jsonify(character_query.serialize()),200

    if request.method == 'DELETE':
        character_query = Character.query.get(character_id)
        if character_query is None:
            raise APIException('User not found. We cant delete it', status_code=404)
        db.session.delete(character_query)
        db.session.commit()
        character_query = Character.query.all()
        all_characters = list(map(lambda x: x.serialize(), character_query))
        return jsonify(all_characters)


# CREATE NEW CHARACTER
@app.route('/character', methods=['POST'])

def create_character():
    body = request.get_json()
    character1 = Character(character_name= body["character_name"],
    hair_color= body["hair_color"], gender= body["gender"])
    db.session.add(character1)
    db.session.commit()
    character_query = Character.query.all()
    all_characters = list(map(lambda x: x.serialize(), character_query))
    return jsonify(all_characters)




# --------PLANETS -----------------



# GET ALL PLANETS
@app.route('/planet', methods=['GET'])
def get_all_planets():

    planet_query = Planet.query.all()
    all_planet = list(map(lambda x: x.serialize(), planet_query))
    return jsonify(all_planet)


# CREATE NEW PLANET
@app.route('/planet', methods=['POST'])
def create_planet():
    body = request.get_json()
    planet1 = Planet(planet_name= body["planet_name"],
    diameter= body["diameter"], rotation_period= body["rotation_period"])
    db.session.add(planet1)
    db.session.commit()
    planet_query = Planet.query.all()
    all_planets = list(map(lambda x: x.serialize(), planet_query))
    return jsonify(all_planets)


# GET  PUT AND DELETE ONE PLANET
@app.route('/planet/<int:planet_id>', methods=['GET' , 'PUT' ,'DELETE'])
def get_one_planet(planet_id):  

    body = request.get_json()
   
    if request.method == 'PUT':
        planet1 = Planet.query.get(planet_id)

        if planet1 is None:
            raise APIException('User not found', status_code=404)

        if "planet_name" in body:
            planet1.planet_name = body["planet_name"]
        if "diameter" in body:
            planet1.diameter = body["diameter"]
        if "rotation_period" in body:
            planet1.rotation_period = body["rotation_period"]
        db.session.commit()
        return jsonify(planet1.serialize()), 200


    if request.method == 'GET':
        planet_query = Planet.query.get(planet_id)
        return jsonify(planet_query.serialize()),200

    if request.method == 'DELETE':
        planet_query = Planet.query.get(planet_id)
        if planet_query is None:
            raise APIException('User not found. We cant delete it', status_code=404)
        db.session.delete(planet_query)
        db.session.commit()
        planet_query = Planet.query.all()
        all_planets = list(map(lambda x: x.serialize(), planet_query))
        return jsonify(all_planets)



# --------FAVORITES -----------------



# GET USERS
@app.route('/users', methods=['GET'])
def get_all_users():

    users_query = User.query.all()
    all_users = list(map(lambda x: x.serialize(), users_query))
    return jsonify(all_users)


# GET ALL FAVORITE CHARACTERS OF A USER
@app.route('/users/favorites/', methods=['GET'])
def all_favorite_character():
    favorite_character_query = Character_favorites.query.all()
    all_characters_favorites = list(map(lambda x: x.serialize(), favorite_character_query))
    return jsonify(all_characters_favorites)




# ADD FAVORITE CHARACTER
@app.route('/users/favorites/<int:id>', methods=['POST'])
def add_favorite_character(id):

    # favorite_character = Character_favorites(character_id= id,user_id = ?????)

    db.session.add(favorite_character)
    db.session.commit()

    all_characters_favorites = list(map(lambda x: x.serialize(), users_query))
    return jsonify(all_characters_favorites)


# -------TOKEN-----------

#GENERATE TOKEN
@app.route("/token", methods=["POST"])
def create_token():
    email_received = request.json.get("email", None)

    password_received = request.json.get("password", None)
    # Query your database for username and password
    user = User.query.filter_by(email=email_received, password=password_received).first()
    if user is None:
        # the user was not found on the database
        return jsonify({"msg": "Bad email or password"}), 401
    
    # create a new token with the user id inside
    access_token = create_access_token(identity=user.id)
    return jsonify({ "token": access_token, "user_id": user.id })




# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)