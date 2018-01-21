'''
server of the naive_blockchain
Created by Xingfan Xia
@12:24 AM 01-21-2018
'''
from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
