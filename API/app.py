import flask
import flask-smorest
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)