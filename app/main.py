import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from openai import OpenAI


# Khởi tạo app 1 lần duy nhất
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Khởi tạo OpenAI Client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"response": None}
    )

@app.post("/chatbot", response_class=HTMLResponse)
async def chat(request: Request, message: str = Form(...)):
    try:
        response = client.responses.create(
            model="gpt-5.4",
            input=message
        )
        bot_response = response.output_text
    except Exception as e:
        bot_response = f"Lỗi: {str(e)}"

    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={
            "user_message": message, 
            "response": bot_response
        }
    )