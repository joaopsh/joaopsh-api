from flask import request
from flask_restful import Resource
from models.post_model import  PostModel
from schemas.post_schema import PostSchema
from libs.text_resource import TextResource

post_schema = PostSchema()

class PostResource(Resource):
    @classmethod
    def get(cls, post_id: int):
        post = PostModel.find_by_id(post_id)

        if post:
            return post_schema.dump(post), 200

        return {"message": TextResource.get_text('resource_not_found')}, 404

class PostListResource(Resource):
    @classmethod
    def post(cls):
        post = post_schema.load(request.get_json())

        try:
            post.save_to_db()
        except:
            return {"message": TextResource.get_text('internal_server_error')}, 500

        return post_schema.dump(post), 201
