from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,DateTime , Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


# Base = declarative_base()





class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(10), unique=True, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False, default= True)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Character(db.Model):
    __tablename__ = 'character'
    character_id = db.Column(db.Integer, primary_key=True) 
    character_name = db.Column(db.String(250),nullable=False)
    hair_color = db.Column(db.String(100))
    eye_color = db.Column(db.String(100))
    skin_color = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    yob = db.Column(db.DateTime)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    description = db.Column(db.Text(400))
    homeworld = db.Column(db.String(250))
    character_favorites = relationship('Character_favorites', backref='Character', lazy=True)


    # tell python how to print the class object on the console
    def __repr__(self):
        return '<Character %r>' % self.character_name

    # tell python how convert the class object into a dictionary ready to jsonify
    def serialize(self):
        return {
            "character_id" : self.character_id,
            "name": self.character_name,
            "hair_color": self.hair_color,
            'gender' : self.gender
          
        }




class Planet(db.Model):
    __tablename__ = 'planet'
    planet_id = Column(Integer, primary_key=True)
    planet_name = Column(String(200))
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    Orbital_period = Column(Integer)
    gravity = Column(String(200))
    population = Column(Integer)
    climate = Column(String(200))
    terrain = Column(String(200))
    description = Column(Text(400))
    url = Column(String(200))
    planet_favorites = relationship('Planet_favorites', backref='Planet', lazy=True)


        # tell python how to print the class object on the console
    def __repr__(self):
        return '<Planet %r>' % self.planet_name

    # tell python how convert the class object into a dictionary ready to jsonify
    def serialize(self):
        return {
            "planet_name": self.planet_name,
            "diameter": self.diameter,
            'rotation_period' : self.rotation_period
        }


class Starship(db.Model):
    __tablename__ = 'starship'
    starship_id = Column(Integer,primary_key=True)
    model = Column(String(200))
    class_type = Column(String(200))
    manufacturer = Column(String(200))
    cost = Column(Integer)
    length = Column(Integer)
    crew = Column(Integer)
    speed = Column(Integer)

        # tell python how to print the class object on the console
    def __repr__(self):
        return '<Starship %r>' % self.starship_name

    # tell python how convert the class object into a dictionary ready to jsonify
    def serialize(self):
        return {
            "starship_name": self.starship_name,
            "model": self.model,
            'class_type' : self.class_type
        }


class Character_favorites(db.Model):
    __tablename__ = 'character_favorites'
    favorites_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('character.character_id'), nullable=False)

         # tell python how to print the class object on the console
    def __repr__(self):
        return '<Character_favorites %r>' % self.character_favorite_name

    # tell python how convert the class object into a dictionary ready to jsonify
    def serialize(self):
        return {
            "favorites_id": self.favorites_id,
            "character_id": self.character_id,
            'user_id' : self.user_id
        }


class Planet_favorites(db.Model):
    __tablename__ = 'planet_favorites'
    favorites_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.planet_id'), nullable=False)

            # tell python how to print the class object on the console
    def __repr__(self):
        return '<Planet_favorites %r>' % self.planet_favorite_name

    # tell python how convert the class object into a dictionary ready to jsonify
    def serialize(self):
        return {
            "planet_favorites_id": self.planet_favorites_id,
            "planet_id": self.planet_id,
            'user_id' : self.user_id
        }