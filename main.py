from fastapi import FastAPI
from app.error_handling.index import setup_error_handling
from app.cors.index import cors
from app.posts.routes.index import posts_router

app = FastAPI()

cors(app)
setup_error_handling(app)

app.include_router(posts_router, tags=["Posts"], prefix="/api/posts")


@app.get("/", tags=["Root"])
def root():
    return {"message": "Welcome to FastAPI! Visit /docs for endpoint documentation."}
