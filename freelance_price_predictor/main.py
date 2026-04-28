from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

from price_model import predict_price

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={},
    )


@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    skill: str = Form(...),
    experience: str = Form(...),
    project_type: str = Form(...),
    complexity: str = Form(...),
    hours: int = Form(...),
):
    try:
        price = predict_price(skill, experience, project_type, complexity, hours)
        return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={"price": price},
        )
    except ValueError as e:
        return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={"error": str(e)},
        )
