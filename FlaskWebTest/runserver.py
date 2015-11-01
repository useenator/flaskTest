"""
This script runs the FlaskWebTest application using a development server.

"""



from os import environ
from FlaskWebTest import app

#from FlaskWebTest import views


if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    #db.create_all()
    app.run(HOST, PORT)

