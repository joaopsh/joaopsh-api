from flask import request
from flask_restful import Resource
from models.post_model import  PostModel
from schemas.post_schema import PostSchema
from libs.strings import gettext

post_schema = PostSchema()

class PostResource(Resource):
    @classmethod
    def get(cls, post_id: int):
        post = PostModel.find_by_id(post_id)
        
        if post:
            return post_schema.dump(post).data, 200

        return {"message": gettext("resource_not_found")}, 404

class PostListResource(Resource):
    @classmethod
    def post(cls):
        loaded_post = post_schema.load(request.get_json())
        post = loaded_post.data

        try:
            post.save_to_db()
        except:
            return {"message": gettext("internal_server_error")}, 500

        return post_schema.dump(post).data, 201
