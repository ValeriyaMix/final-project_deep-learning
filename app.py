import os

from detector import detectObject
from PIL import Image
from flask import Flask, render_template, request, send_from_directory


UPLOAD_FOLDER = '/home/valeria/deepapp/uploads'
UPLOAD_FOLDER_NORM = '/home/valeria/deepapp/normpic_uploads'


app = Flask(__name__)
app.config['SECRET_KEY'] = 'I have a dream'





@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = Image.open(request.files['file'].stream)
        file.save(os.path.join("/home/valeria/deepapp/normpic_uploads", "normpic.jpeg"))
        img = detectObject(file)
        return send_from_directory('/home/valeria/deepapp/uploads', "prediction.jpg")
    return render_template('index.html')


@app.route('/norm_uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('/home/valeria/deepapp/normpic_uploads', filename)


@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge, chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


if __name__ == "__main__":
    app.run()
