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

@app.route('/documents/<id>', methods=['GET'])
def get_document(id):
  document = Document.query.get(id)
  del document.__dict__['_sa_instance_state']
  return jsonify(document.__dict__)

@app.route('/documents', methods=['GET'])
def get_documents():
  documents = []
  for document in db.session.query(Document).all():
    del document.__dict__['_sa_instance_state']
    documents.append(document.__dict__)
  return jsonify(documents)

@app.route('/documents', methods=['POST'])
def create_document():
  body = request.get_json()
  db.session.add(Document(body['title'], body['text']))
  db.session.commit()
  return "document created"

@app.route('/documents/<id>', methods=['PUT'])
def update_document(id):
  body = request.get_json()
  db.session.query(Document).filter_by(id=id).update(
    dict(title=body['title'], text=body['text']))
  db.session.commit()
  return "document updated"

@app.route('/documents/<id>', methods=['DELETE'])
def delete_document(id):
  db.session.query(Document).filter_by(id=id).delete()
  db.session.commit()
  return "document deleted"
