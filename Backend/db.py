from flask import Flask
from flask_pymongo import pymongo
from app import app

CONNECTION_STRING = 'mongodb+srv://mannynuovo:tAV6lfklmEnnFerW@cluster0.yurhnqf.mongodb.net/test'
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('heart_disease_prediction')
users = pymongo.collection.Collection(db, 'Users')
