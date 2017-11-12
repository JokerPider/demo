#encoding: utf-8
from flask import Flask
import config

app = Flask(__name__)
app.config.from_object(config)

@aqq.route('/')
def hello_world():
	return "hello world!"

if __name__ == "__main__":
	app.run()