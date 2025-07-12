# backend/main.py

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from backend.db import init_db, insert_order, get_all_orders


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()

class Order(BaseModel):
    section: str
    vendor: str
    item: str
    wait_time: float

@app.get("/orders")
def fetch_orders():
    rows = get_all_orders()
    return [{
        "id": r[0],
        "timestamp": r[1],
        "section": r[2],
        "vendor": r[3],
        "item": r[4],
        "wait_time": r[5]
    } for r in rows]

@app.post("/orders")
def create_order(order: Order):
    insert_order(order.section, order.vendor, order.item, order.wait_time)
    return {"status": "ok"}
