from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import os

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

@app.get("/clases")
async def clases_page(request: Request):
    return templates.TemplateResponse("clases.html", {"request": request})

@app.get("/clases/solicitar/{tipo}")
async def solicitar_page(request: Request, tipo: str):
    return templates.TemplateResponse("solicitar.html", {"request": request, "type": tipo})

class Solicitud:
    tipo: str
    nombre: str
    contacto: str
    mensaje: str
    def __init__(self, tipo, nombre, contacto, mensaje):
        self.tipo = tipo
        self.nombre = nombre
        self.contacto = contacto
        self.mensaje = mensaje
    

@app.post("/clases/solicitar/{tipo}")
async def solicitar(request: Request, tipo: str, name: str = Form(...), contact: str = Form(...), message: str = Form(...)):
    solicitud = Solicitud(tipo, name, contact, message)
    i = 0
    while os.path.exists("%s" % i):
        i += 1

    with open("./solicitudes/%s" % i, "w") as file:
        file.write("Solicitante: %s\n" % name)
        file.write("Tipo de clase: %s\n" % tipo)
        file.write("Contacto: %s\n" % contact)
        file.write("Mensaje adicional: %s\n" % message) 

    return templates.TemplateResponse("exito.html", {"request": request})
    
