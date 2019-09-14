import os

class Config(object):
    SECRET_KEY = os.env.get('SECRET_KEY') or 'you-will-never-guess-this'


