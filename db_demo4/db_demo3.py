#encoding: utf-8
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


article_tag = db.Table('article_tag',
	db.Column('article_id', db.Integer, db.ForeignKey('article.id'), primary_key=True),
	db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
	)


class Article(db.Model):
	__tablename__ = 'article'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	title = db.Column(db.String(100), nullable=False)
	content = db.Column(db.Text, nullable=False)


class Tag(db.Model):
	__tablename__ = 'tag'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(100), nullable=False)


db.create_all()  #真正创建SQL

@app.route('/')
def index():

	return 'hello world!!'


if __name__ == '__main__':
	app.run(debug=True)