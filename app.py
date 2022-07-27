from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blogdb.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Suppress the flask dictionary keys sorting and forces to respect the defined schema order.
app.config['JSON_SORT_KEYS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

from models.database import Post
from models.schemas import post_schema, posts_schema


@app.route('/')
def home():
	return redirect(url_for('documentation'))


@app.route('/api/docs/')
def documentation():
	return render_template('documentation.html')


@app.get('/api/posts/')
def get_posts():
	response = posts_schema.jsonify(Post.query.all())
	return response, 200


@app.post('/api/posts/')
def create_post():
	data = request.json
	payload = Post(
		title=data.get('title'),
		body=data.get('body'),
		status=data.get('status'),
		featured=data.get('featured')
	)
	db.session.add(payload)
	try:
		db.session.commit()
		return post_schema.jsonify(payload), 201
	except IntegrityError:
		db.session.rollback()
		return {"message": "duplicate post found"}, 409


@app.get('/api/posts/<int:pk>')
def get_post(pk):
	response = post_schema.jsonify(Post.query.get_or_404(pk))
	return response, 200


@app.patch('/api/posts/<int:pk>')
def update_post(pk):
	payload = request.json
	query = Post.query.get_or_404(pk)
	if 'title' in payload:
		query.title = payload.get('title')
		query.slug = re.sub('[ ]', '-', query.title.lower())
	if 'body' in payload:
		query.body = payload.get('body')
	if 'status' in payload:
		query.status = payload.get('status')
	if 'featured' in payload:
		query.featured = payload.get('featured')
	db.session.commit()
	return post_schema.jsonify(payload), 200


@app.delete('/api/posts/<int:pk>')
def delete_post(pk):
	todo = Post.query.get_or_404(pk)
	db.session.delete(todo)
	db.session.commit()
	return {}, 204


if __name__ == '__main__':
	app.run()
