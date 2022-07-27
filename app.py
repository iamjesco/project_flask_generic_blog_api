from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blogdb.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Suppress the flask dictionary keys sorting and forces to respect the defined schema order.
app.config['JSON_SORT_KEYS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


@app.route('/')
def home():
	return redirect(url_for('documentation'))


@app.route('/api/docs/')
def documentation():
	return render_template('documentation.html')


@app.get('/api/posts/')
def get_posts():
	# response = todos_schema.jsonify(Todos.query.all())
	# return response, 200
	return {"message": "all posts"}, 200


@app.post('/api/posts/')
def create_post():
	# response = todos_schema.jsonify(Todos.query.all())
	# return response, 200
	return {"message": "post created"}, 201


@app.get('/api/posts/<int:pk>')
def get_post(pk):
	# response = todos_schema.jsonify(Todos.query.all())
	# return response, 200
	return {"message": "single post"}, 200


@app.patch('/api/posts/<int:pk>')
def update_post(pk):
	# response = todos_schema.jsonify(Todos.query.all())
	# return response, 200
	return {"message": "post updated"}, 200


@app.delete('/api/posts/<int:pk>')
def delete_post(pk):
	# response = todos_schema.jsonify(Todos.query.all())
	# return response, 200
	return {"message": "post deleted"}, 204


if __name__ == '__main__':
	app.run()
