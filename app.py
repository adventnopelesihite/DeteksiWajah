import os
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import cv2 #pemanggilan library

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def detec(wajah):
        img = cv2.imread('filename') #untuk membaca file Foto

        wajah = cv2.CascadeClassifier('face-detect.xml') #untuk melakukan load XML untuk medeteksi wajah
        gray = cv2.cvtColor(filename, cv2.COLOR_BGR2GRAY) #menterjemahkan foto dalam bntuk gray       



        wajah = wajah.detectMultiScale(gray, 1.3, 5) #untuk mendetek gray yang ada difotonya


        for (x,y,w,h) in wajah: #perulangan For untuk pembacaan atau perulangan pada foto, pada sumbuh x,y,w,h
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2) #untuk mendeteksi gray pada sumbuh x,y

            cv_warna = img[y:y+h, x:x+w]
            cv_gray = gray[y:y+h, x:x+w]



        cv2.imshow('Foto Deteksi Wajah', img) #untuk memunculkan foto yang kita baca tadi

        result=cv2.imwrite('static/uploads/filename', img)
        return render_template('index.html', filename=filename)

        cv2.waitKey(0) #tidak ada jeda, langsung dimunculkan
        cv2.destroyAllWindows() #setelah integrasi diatas berhasil,deteksinya dijalankan


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
    if file not in request.files:
        flash('No file part')
        return redirect(request.url)
        file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('Image successfully uploaded and displayed below')
        flash('Namanya ' + filename)     
        return render_template('index.html', filename=filename)
        

    else:
        flash('Allowed image types are -> png, jpg, jpeg, gif')
        return redirect(request.url)




if __name__ == '__main__':
    app.run(debug=True)