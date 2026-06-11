# /config.py

import os

basedir = os.path.abspath(os.path.dirname(__file__))

debug = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:123456@127.0.0.1:3306/audio_novels"
SQLALCHEMY_TRACK_MODIFICATIONS = False


