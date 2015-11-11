import os
from flask import Flask, request, redirect, url_for,render_template
from werkzeug import secure_filename

from app import app
import models
from pagination import Pagination
#UPLOAD_FOLDER = r"E:\uploads"
#UPLOAD_FOLDER = r"E:\Documents\Visual Studio 2015\Projects\FlaskWebTest\FlaskWebTest\FlaskWebTest\uploads"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
ALLOWED_IMAGES_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])#set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

#app = Flask(__name__)

# Set this configuration to absolute or relative path to upload directory.
UPLOAD_FOLDER = "E:\Documents\Visual Studio 2015\Projects\FlaskWebTest\FlaskWebTest\FlaskWebTest\static\uploads"
COVER_FOLDER = "E:\Documents\Visual Studio 2015\Projects\FlaskWebTest\FlaskWebTest\FlaskWebTest\static\cover"


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
    """Returs True or false if a file is in ALLOWED_FILES"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_IMAGES_EXTENSIONS#ALLOWED_EXTENSIONS


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


#UPLOAD_FOLDER = "E:\Documents\Visual Studio 2015\Projects\FlaskWebTest\FlaskWebTest\FlaskWebTest\static\butlerIMG"
@app.route('/tomatoss/',methods=['GET','POST'])
def tomatoss():
    listimg=os.listdir("E:\\Documents\\Visual Studio 2015\\Projects\\FlaskWebTest\\FlaskWebTest\\FlaskWebTest\\static\\cover\\tmp\\")
    print(listimg)
    listimages=[]
    for item in listimg:
        if allowed_file(item):
            listimages.append(item)
    return render_template('layoutMovie.html',listdir=listimages,dirname='/static/cover/tmp/',
                           title='Movies list')
    #return render_template('layoutMovie.html',listdir=listimg,dirname='/static/butlerIMG/')
    #return render_template('layoutB.html',listdir=listimg,dirname='/static/uploads/')



@app.route('/tomatos/',methods=['GET','POST'])
@app.route('/tomatos/<int:end>',methods=['GET','POST'])
def tomatos(end=6):
    listimg=os.listdir("E:\\Documents\\Visual Studio 2015\\Projects\\FlaskWebTest\\FlaskWebTest\\FlaskWebTest\\static\\cover\\tmp\\")
    #print(listimg)
    
    listimages=[]
    for item in listimg[0:end]:
        if allowed_file(item):
            listimages.append(item)
    #print(request.values.get('page'))
    #print(request.args.get('page', None))
    return render_template('layoutMoviePagination.html',listdir=listimages,dirname='/static/cover/tmp/',
                           title='Movies list')

    #if request.method == 'POST':
       
    #return render_template('layoutMovie.html',listdir=listimg,dirname='/static/butlerIMG/')
    #return render_template('layoutB.html',listdir=listimg,dirname='/static/uploads/')


    

@app.route('/tomatosChild/<int:page>')
def tomatosChild(page=1):
    listimg=os.listdir("E:\\Documents\\Visual Studio 2015\\Projects\\FlaskWebTest\\FlaskWebTest\\FlaskWebTest\\static\\cover\\tmp\\")
    #print(listimg)
    total=len(listimg)
    PER_PAGE=6
    # set up the pagination params, set count later
    p = Pagination(total=total,per_page=PER_PAGE, current_page=page)
    start=p.start
    end=start+PER_PAGE
    listimages=[]
    for item in listimg[start:end]:
        if allowed_file(item):
            listimages.append(item)

    
    ##timeline = RedisTimeline.find_paginated(p)
    return render_template('layoutMoviePaginationChild.html',listdir=listimages,dirname='/static/cover/tmp/',
                           title='Movies list', pagination=p)

    # set up the pagination params, set count later
    #p = Pagination(per_page=10, current_page=page)
    #timeline = RedisTimeline.find_paginated(p)
    # pass the pagination object to the view, so a list of links can be displayed
    #return render_template('index.html', timeline=timeline, pagination=p)



'''

@app.route('/butler/',methods=['GET','POST'])
def butler():
    listimg=os.listdir("E:\Documents\Visual Studio 2015\Projects\FlaskWebTest\FlaskWebTest\FlaskWebTest\static\cover")#UPLOAD_FOLDER)
    #print(listimg)
    #listimages=[]
    for item in listimg:
        if not allowed_file(item) or not os.path.isdir(COVER_FOLDER+item):
            listimg.remove(item)

        print("list of images")
        print(listimg)
    return render_template('layoutButler.html',listdir=listimg,dirname='/static/cover/',
                               title='Movies list')
'''



@app.route('/butler/',methods=['GET','POST'])
def butler():
    listimg=os.listdir("E:\Documents\Visual Studio 2015\Projects\FlaskWebTest\FlaskWebTest\FlaskWebTest\static\cover")#UPLOAD_FOLDER)
    #print(listimg)
    listimages=[]
    for item in listimg:
        if allowed_file(item):
            listimages.append(item)
        print("list of images")
        print(listimages)
    return render_template('layoutButler.html',listdir=listimages,dirname='/static/cover/',
                               title='Movies list')   



@app.route('/butlerdetails/',methods=['GET','POST'])
def butlerDetails():
    listimg=os.listdir("E:\Documents\Visual Studio 2015\Projects\FlaskWebTest\FlaskWebTest\FlaskWebTest\static\cover")#UPLOAD_FOLDER)
    print(listimg)
    
    return render_template('layoutButlerChild.html',listdir=listimg,dirname='/static/cover/',
                           title='Movies Details')
    #return render_template('layoutMovie.html',listdir=listimg,dirname='/static/butlerIMG/')
    #return render_template('layoutB.html',listdir=listimg,dirname='/static/uploads/')  




# This is a simplified class that uses Redis

class RedisTimeline(object):
    
    @classmethod
    def find_paginated(self, pagination):
        # self.count returns the total number of items in the timeline
        pagination.total = self.count()
        # pass in the pagination params which can be used as offset
        timeline = self.find(limit=pagination.per_page, start=pagination.start)
        return timeline
        
    @classmethod
    def find(self, limit=100, start=0):
        """ZREVRANGE foo <$OFFSET> <$OFFSET + $LIMIT - 1> will yield correct results if both OFFSET and LIMIT are assumed to be zero-based.
        So 0/0 gives you the full range, then offset 10 limit 10 will give you items 11 to 20."""
        ids = r.zrevrange('myrediskey', start, start + limit - 1)
        
        # do something with ids and generate a timeline object
        return timeline

