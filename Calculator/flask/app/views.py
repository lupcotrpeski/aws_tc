import os
from flask import flash, request, redirect, render_template, request, current_app, send_from_directory
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length
from werkzeug.utils import secure_filename

from app import app
from lib.generateReport import GenerateReport

# Variable declaration
allowedExtensions = {'csv'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowedExtensions

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods = ['GET', 'POST'])
def indexPost(fileName = None):
    fileName='xero.csv'
    print("Index Filename: ",fileName)
    className = request.form['className']
    classLocation = request.form['classLocation']
    classType = request.form['classType']
    trainer = request.form['trainer']
    startDate = request.form['startDate']
    endDate = request.form['endDate']
    filePath = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    response = GenerateReport(filePath, fileName, className, classLocation, classType, trainer, startDate, endDate).generateReport()
    print("Response: ", response)
    return render_template('index.html', response=response)
	
@app.route('/uploads', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        if f.filename == '':
           flash('No selected file')
           return redirect(request.url)
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join("app/" + app.config['UPLOAD_FOLDER'], filename))
    
    return render_template('index.html', fileName=filename, response='file uploaded successfully')

@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    # Appending app path to upload folder path within app root folder
    uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    # Returning file from appended path
    print(uploads)
    return send_from_directory(directory=uploads, filename=filename)