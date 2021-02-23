from flask import request, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length
from werkzeug.utils import secure_filename

from app import app
from lib.generateReport import GenerateReport

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods = ['GET', 'POST'])
def indexPost(fileName = None):
    print("Index FileName: ",fileName)
    className = request.form['className']
    classLocation = request.form['classLocation']
    classType = request.form['classType']
    trainer = request.form['trainer']
    startDate = request.form['startDate']
    endDate = request.form['endDate']
    response = GenerateReport(fileName, className, classLocation, classType, trainer, startDate, endDate).generateReport()
    print("Response: ", response)
    return render_template('index.html', response=response)
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      print("Upload FileName: ",f.filename)
      return render_template('index.html', fileName=f.filename, response='file uploaded successfully')