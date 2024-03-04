
import os
import random
import string
from apps.home import blueprint
from flask import current_app, flash, redirect, render_template, request, url_for
from flask_login import login_required
from jinja2 import TemplateNotFound
from .util import allowed_file, get_all_processed_files, get_processed_file_path, get_randomized_filename, get_upload_filepath, get_yolo_processed_folder_path, get_yolo_weights_path, is_image
from apps.yolov5.detect import run
from ultralytics import YOLO
@blueprint.route('/index')
@login_required
def index():
    images, vidoes = get_all_processed_files()
    
    destination_folder = os.path.join(current_app.config["STATIC_FOLDER"],current_app.config["UPLOAD_FOLDER"])
    return render_template('home/results.html',images=images,vidoes=vidoes,destination_folder=destination_folder)

@blueprint.route("/new-experiment")
@login_required
def new_experiment():
    
    return render_template('home/new_experiment.html')



@blueprint.route("/process", methods=['POST'])
@login_required
def process_experiment():
    if 'file' not in request.files:
            flash('No file part')
            return redirect(url_for("home_blueprint.new_experiment"))
        
    req_file = request.files['file']
    if req_file.filename == '':
            flash('No selected file')
            return redirect(request.url)
    if req_file and allowed_file(req_file.filename):
        req_file.filename = get_randomized_filename(req_file)
        orginal_file_path = get_upload_filepath(req_file.filename)                
        req_file.save(orginal_file_path)
        
        v5_filepath = get_yolo_processed_folder_path("v5")
        
        run(weights=get_yolo_weights_path("v5"),conf_thres=0.25,
                imgsz=(640,640),
                source=orginal_file_path, 
                project=v5_filepath,
                name="result",
                exist_ok=True
                )
        
        v8_filepath =get_yolo_processed_folder_path("v8")
            
        model = YOLO(get_yolo_weights_path("v8"),)
        result = model.predict(source=orginal_file_path,
                project=v8_filepath,
                name="result",
                exist_ok=True,
                save=True
                )
        
    if is_image(req_file.filename):
            
            
                return redirect(
                    url_for("home_blueprint.current_results",result_type="image",file_name=req_file.filename,
                            )
                    )
    else:
            
                return redirect(
                    url_for("home_blueprint.current_results",result_type="video",file_name=req_file.filename,
                            )
                    )
        







@blueprint.route("/current-result/<result_type>/<file_name>", methods=['GET'])
@login_required
def current_results(result_type,file_name):
    
    
    v5_file_path = get_processed_file_path("v5",file_name)
    v8_file_path = get_processed_file_path("v8",file_name)

    
    return render_template('home/current-result.html', v5_file_path=v5_file_path,v8_file_path=v8_file_path, result_type=result_type)

@blueprint.route("/results", methods=['GET'])
@login_required
def results():
    images, vidoes = get_all_processed_files()
    
    destination_folder = os.path.join(current_app.config["STATIC_FOLDER"],current_app.config["UPLOAD_FOLDER"])
   
    return render_template('home/results.html',images=images,vidoes=vidoes,destination_folder=destination_folder)