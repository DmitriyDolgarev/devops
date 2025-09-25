from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import asyncio
from datetime import datetime
from datetime import timedelta
from typing import List

app = FastAPI()

origins = [
    "http://127.0.0.1:5500",  # Разрешить origin вашего клиентского приложения
    "http://localhost:5500", # Ещё один распространенный вариант для разработки
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы (GET, POST, PUT, DELETE, и т.д.)
    allow_headers=["*"],  # Разрешить все заголовки
)

global count

count = 0

@app.get("/get/")
def read_root():
    global count

    return {
        "value": count
    }

@app.get("/plus/")
def read_root():
    global count

    count = count + 1

    return {
        "value": count
    }

@app.get("/quatro/")
async def process_number():
    global count

    count = count * count

    return {
        "value": count
    }

@app.get("/reset/")
async def process_number():
    global count

    count = 0

    return {
        "value": count
    }