import hug

from routes import user

router = hug.route.API(__name__)

@hug.get('/')
def hello():
    return 'Hello World!'

hug.extend_api('/users')(lambda: [user])
