#encoding: utf-8

from flask import Flask

app = Flask(__name__)

@aqq.route('/')
def hello_world():
	return "hello world!"

if __name__ == "__main__":
	app.run()