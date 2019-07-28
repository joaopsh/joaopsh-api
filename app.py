import settings
from debugger import Debugger
from flask import Flask
from flask_restful import Api
from resources.post_resource import PostResource, PostListResource
from db import db
from ma import ma

IS_DEBUGGER_ATTATCH_ENABLED = settings.ENABLE_DEBUGGER_ATTACH == 'True'
IS_DEBUG_ENABLED = settings.DEBUG == 'True'

app = Flask(__name__)
app.config.from_envvar("APPLICATION_SETTINGS")

api = Api(app)

api.add_resource(PostListResource, '/post')
api.add_resource(PostResource, '/post/<int:post_id>')

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)

    if IS_DEBUGGER_ATTATCH_ENABLED:
        Debugger.enable_debugger_attach()

    app.run(host='0.0.0.0',
            port=5000, 
            debug=IS_DEBUG_ENABLED and not IS_DEBUGGER_ATTATCH_ENABLED)
