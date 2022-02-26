from fastapi import FastAPI, Response
from fastapi.params import Body
from pydantic import BaseModel
from pydantic.fields import Optional
from random import randrange


class Post(BaseModel):
    title :str
    content:str
    rating: Optional[int] = None

app = FastAPI()

my_posts = [{"title ":"this is the first post", "content ": "Sample content","id":1},
            {"title ":"My fav food", "content ": "Any food","id":2}]
def find_posts(id):
    for p in my_posts:
        if p['id'] == id:
            return p
@app.get("/")
async def root():
    return {"message" : "Hello World, welcome t my api"}

@app.get("/posts")
def getposts():
    return {"data": my_posts}

@app.post("/posts")
def displayPosts(new_post :Post):
    post_dict = new_post.dict()
    post_dict['id'] = randrange(0,1000000)
    my_posts.append(post_dict)
    print(new_post.rating)
    return {new_post}


@app.get("/about")
async def root():
    return {"message" : "about us"}

@app.get("/posts/{id}")
def findPost(id: int, responseCode: Response):
    post = find_posts(id)
    if not post:
        responseCode.status_code(404)
    print(post)
    return post