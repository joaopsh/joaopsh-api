from debugger import Debugger
from flask import Flask, jsonify
from flask_restful import Api

import settings
from resources.post_resource import PostResource, PostListResource
from db import db
from ma import ma
from handlers.error_handler import error_handler
from libs.text_resource import TextResource
from libs.language import Language


app = Flask(__name__)
app.config.from_envvar("APPLICATION_SETTINGS")
app.register_error_handler(Exception, error_handler)

api = Api(app)
api.add_resource(PostListResource, '/post')
api.add_resource(PostResource, '/post/<int:post_id>')

lang = Language(app)

@app.before_first_request
def create_tables():
    db.create_all()

@lang.default_language
def default_language():
    return 'en-us'

@lang.allowed_languages
def allowed_languages():
    return ['en-us', 'pt-br']

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    
    TextResource.init_app(app)

    if settings.ENABLE_DEBUGGER_ATTACH:
        Debugger.enable_debugger_attach()

    app.run(host='0.0.0.0',
            port=5000, 
            debug=settings.DEBUG and not settings.ENABLE_DEBUGGER_ATTACH)

