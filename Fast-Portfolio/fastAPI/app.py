from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def portfolio(request: Request):
    user_info = {
        "name": "Saurabh Kahar",
        "bio": "I'm a passionate developer with expertise in Python, Django, and Cloud technologies.",
        "skills": ["Python", "Django", "FastAPI", "Cloud Computing", "AWS", "HTML", "CSS", "JavaScript"],
        "projects": [
            {"name": "Personal Finance Tracker", "description": "A Django web app to track income, expenses, and budgets."},
            {"name": "YouTube Downloader", "description": "A simple YouTube video downloader built using Django and pytube."},
            {"name": "Tic-Tac-Toe Game", "description": "A Python game using Tkinter with multiplayer support."}
        ]
    }
    return templates.TemplateResponse("portfolio.html", {"request": request, "user_info": user_info})


@app.post("/contact", response_class=HTMLResponse)
async def contact_me(request: Request, name: str = Form(...), email: str = Form(...), message: str = Form(...)):
    # Simulate contact form submission (for now, just print the data)
    print(f"Message from {name} ({email}): {message}")
    return templates.TemplateResponse("portfolio.html", {"request": request, "submitted": True})
