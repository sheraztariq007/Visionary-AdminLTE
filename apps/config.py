# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os, random, string


PROJECT_TITLE = "Visionary"
PROJECT_SUB_TITLE = "A better surveillance for furture"

basedir = os.path.abspath(os.path.dirname(__file__))

    # Assets Management
ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')

    # Set up the App SECRET_KEY
SECRET_KEY  = os.getenv('SECRET_KEY', None)
if not SECRET_KEY:
        SECRET_KEY = ''.join(random.choice( string.ascii_lowercase  ) for i in range( 32 ))    

SQLALCHEMY_TRACK_MODIFICATIONS = False

DB_ENGINE   = os.getenv('DB_ENGINE'   , None)
DB_USERNAME = os.getenv('DB_USERNAME' , None)
DB_PASS     = os.getenv('DB_PASS'     , None)
DB_HOST     = os.getenv('DB_HOST'     , None)
DB_PORT     = os.getenv('DB_PORT'     , None)
DB_NAME     = os.getenv('DB_NAME'     , None)

USE_SQLITE  = True 

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3') 
        
        
ALLOWED_IMAGE_EXTENSIONS = ["jpg", "jpeg", "png", "gif", "svg", "webp", "ico", "tiff", "tif"]
ALLOWED_VIDEO_EXTENSIONS= [ "mp4", "webm", "mov", "flv", "avi", "wmv", "mpg"]
V5_WEIGHTS_FOLDER=  "weights/best.pt"
V8_WEIGHTS_FOLDER= "weights/best_M.pt"


UPLOAD_FOLDER = "uploaded_files"
STATIC_FOLDER=  "static"
PROCESSED_FOLDER =  "processed_files"
    



