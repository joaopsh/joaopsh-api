from ma import ma
from models.post_model import PostModel


class PostSchema(ma.ModelSchema):
    class Meta:
        model = PostModel
        load_only = ("id")
