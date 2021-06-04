import os
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


<<<<<<< HEAD

=======
>>>>>>> e0c85b7a6ba178f3f92204bff3ad6f81fe838ed7
UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def post():
<<<<<<< HEAD
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
=======
    if file not in request.files:
        flash('No file part')
        return redirect(request.url)
        file = request.files['file']
>>>>>>> e0c85b7a6ba178f3f92204bff3ad6f81fe838ed7
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
<<<<<<< HEAD
        
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        flash('Image successfully uploaded and displayed below')
        flash('Nama ' + filename)
        return render_template('index.html', filename=filename)
        
=======
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('Image successfully uploaded and displayed below')
        flash('Namanya ' + filename)     
        return render_template('index.html', filename=filename)
        

>>>>>>> e0c85b7a6ba178f3f92204bff3ad6f81fe838ed7
    else:
        flash('Allowed image types are -> png, jpg, jpeg, gif')
        return redirect(request.url)




if __name__ == '__main__':
    app.run(debug=True)
