from bson import ObjectId
from fastapi.encoders import jsonable_encoder
from app.database.index import db
from app.posts.models.index import Post
from app.utils.index import custom_encoders
from app.error_handling.index import NotFoundError


def get_posts_controller():
    return jsonable_encoder(list(db.posts.find()), custom_encoder=custom_encoders)


def create_post_controller(post: Post):
    result = db.posts.insert_one({"_id": ObjectId(), **post.model_dump()})
    return {"_id": str(result.inserted_id), **post.model_dump()}


def update_post_controller(post_id: str, update_post: Post):
    result = db.posts.find_one_and_update(
        {"_id": ObjectId(post_id)},
        {"$set": update_post.model_dump(exclude_none=True)},
        return_document=True
    )
    return jsonable_encoder(result, custom_encoder=custom_encoders)


def delete_post_controller(post_id: str):
    result = db.posts.delete_one({"_id": ObjectId(post_id)})
    if result.deleted_count == 0:
        raise NotFoundError("Post not found")
    return {"detail": "Post successfully deleted"}
