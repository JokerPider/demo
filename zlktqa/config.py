#encoding: utf-8
import os

DEBUG = True
SECRET_KEY = os.urandom(24)


HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'demo'
USERNAME = 'root'
PASSWORD = 'caomu888'
DB_URI = 'mysql://%s:%s@%s/%s' % (USERNAME, PASSWORD, HOSTNAME, DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI