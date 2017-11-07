#encoding: utf-8
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.String(100), nullable=True)


class Article(db.Model):
	__tablename__ = 'article'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	title = db.Column(db.String(100), nullable=False)
	content = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	author = db.relationship('User', backref=db.backref('articles'))


db.create_all()  #真正创建SQL

@app.route('/')
def index():
	# 添加用户
	# user1 = User(username='Joker')
	# db.session.add(user1)
	# db.session.commit()

	# 添加文章
	# article = Article(title='hello', content='你好世界', user_id=1)
	# db.session.add(article)
	# db.session.commit()

	article = Article.query.filter(Article.title == 'hello').first()
	print article.author.username

	return 'hello world!!'


if __name__ == '__main__':
	app.run(debug=True)