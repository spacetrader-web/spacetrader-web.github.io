import pymongo
from flask import Flask, request, jsonify, json
from pymongo import MongoClient

application = Flask(__name__)

client = pymongo.MongoClient("mongodb://admin:st@spacetrader-cluster-shard-00-00-yik2d.gcp.mongodb.net:27017,spacetrader-cluster-shard-00-01-yik2d.gcp.mongodb.net:27017,spacetrader-cluster-shard-00-02-yik2d.gcp.mongodb.net:27017/test?ssl=true&replicaSet=spacetrader-cluster-shard-0&authSource=admin&retryWrites=true")
db = client.test
print(db)
