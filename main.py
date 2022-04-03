from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates/")

@app.get("/")
async def main_page(request: Request):
    return templates.TemplateResponse("main.html", {"request": request}) 

@app.get("/about")
async def about_page(request: Request):
    return templates.TemplateResponse("about.html", {"request": request}) 

@app.get("/videos")
async def videos_page(request: Request):
    return templates.TemplateResponse("videos.html", {"request": request})
