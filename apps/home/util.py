import os
from flask import current_app
import random,string

def allowed_file(filename):
    print(current_app.config)
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config.get('ALLOWED_IMAGE_EXTENSIONS')+current_app.config.get('ALLOWED_VIDEO_EXTENSIONS')
           


def is_image(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config.get('ALLOWED_IMAGE_EXTENSIONS')
           
def is_video(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config.get('ALLOWED_VIDEO_EXTENSIONS')
           
def get_randomized_filename(req_file):
    extension = req_file.filename.split('.')[-1]
    filename_prefix = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    return filename_prefix+"."+extension
            
def get_upload_filepath(filename):
    return os.path.join("apps",current_app.config["STATIC_FOLDER"],current_app.config['UPLOAD_FOLDER'], filename)


def get_yolo_processed_folder_path(version):
    return os.path.join("apps",current_app.config["STATIC_FOLDER"],current_app.config['PROCESSED_FOLDER'], version)


def get_yolo_weights_path(version):
    return os.path.join("apps",current_app.config["STATIC_FOLDER"],"assets","weights", version+".pt")


def get_processed_file_path(version,file_name):
    return os.path.join(current_app.config["STATIC_FOLDER"],current_app.config["PROCESSED_FOLDER"], version,"result",file_name)

def get_all_processed_files():
    upload_files =  os.listdir(os.path.join("apps",current_app.config["STATIC_FOLDER"],current_app.config["UPLOAD_FOLDER"]))
    
    images =[ upload_file for upload_file in upload_files if is_image(upload_file) ]
    videos =[upload_file for upload_file in upload_files if is_video(upload_file)]

    return images, videos