#encoding: utf-8
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

class Article(db.Model):
	__tablename__ = 'article'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	title = db.Column(db.String(100), nullable=False)
	content = db.Column(db.Text, nullable=False)

db.create_all()  #真正创建SQL

@app.route('/')
def index():

	# # 增加
	# article1 = Article(title='aaa', content='bbb')
	# db.session.add(article1)
	# # 事物
	# db.session.commit()

	# 查
	# res = Article.query.filter(Article.title == 'aaa').first()
	# print 'title: %s' % res.title

	# # 改
	# # 1.查出需要修改的数据
	# res = Article.query.filter(Article.title == 'aaa').first()
	# # 2.修改
	# res.title = 'abc'
	# # 3.提交事物
	# db.session.commit()

	# 删除
	# 1.查出需要删除的数据
	# 2.删除
	# 3.提交
	# res = Article.query.filter(Article.title == 'abc').first()
	# db.session.delete(res)
	# db.session.commit()
	# return 'hello world!!'


if __name__ == '__main__':
	app.run(debug=True)