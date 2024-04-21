from fastapi import APIRouter, Depends
from app.posts.models.index import Post
from app.auth.index import verify_token
from app.posts.controllers.index import (
    get_posts_controller, create_post_controller,
    update_post_controller, delete_post_controller
)

posts_router = APIRouter()
router_dependencies = [Depends(verify_token)]


@posts_router.get('/')
def get_posts():
    return get_posts_controller()


@posts_router.post('/', dependencies=router_dependencies)
def create_post(post: Post):
    return create_post_controller(post)


@posts_router.patch('/{post_id}', dependencies=router_dependencies)
def update_post(post_id: str, update_post: Post):
    return update_post_controller(post_id, update_post)


@posts_router.delete('/{post_id}', dependencies=router_dependencies)
def delete_post(post_id: str):
    return delete_post_controller(post_id)
