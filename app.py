from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

class Document(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(128), unique=True, nullable=False)
  text = db.Column(db.String(512), unique=True, nullable=False)

  def __init__(self, title, text):
    self.title = title
    self.text = text

db.create_all()

