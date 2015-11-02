import os
from flask import Flask, request, redirect, url_for,render_template
from werkzeug import secure_filename

from app import app
#UPLOAD_FOLDER = r"E:\uploads"
#UPLOAD_FOLDER = r"E:\Documents\Visual Studio 2015\Projects\FlaskWebTest\FlaskWebTest\FlaskWebTest\uploads"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

#app = Flask(__name__)

# Set this configuration to absolute or relative path to upload directory.
UPLOAD_FOLDER = "E:\Documents\Visual Studio 2015\Projects\FlaskWebTest\FlaskWebTest\FlaskWebTest\static\uploads"


def init_app(app):
    "Initialize app object. Create upload folder if it does not exist."
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    


#app = Flask(__name__)
#app.config.from_object(__name__)
init_app(app)
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            listdir=os.listdir(UPLOAD_FOLDER) #"C:\Users\Hmed\Pictures\Wallpapers")
            print(os.path.dirname(os.path.abspath(__file__)))
            #return render_template('upload.html',listdir=listdir,dirname=os.path.dirname(os.path.abspath(__file__))+'\\static\\uploads\\')
            return render_template('upload.html',listdir=listdir,dirname='/static/uploads/')
            #return "file "+os.path.join(app.config['UPLOAD_FOLDER'], filename)+" uploaded"
            #redirect(url_for('uploaded_file',filename=filename))
    return render_template('upload.html')
    