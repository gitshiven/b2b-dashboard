# backend/simulator.py

import time
import random
import requests

API_URL = "http://127.0.0.1:8000/orders"

sections = ['A1', 'A2', 'A3', 'B1', 'B2', 'C1']
vendors = ['GrillZone', 'DrinkHub', 'PizzaPals']
items = ['Burger', 'Fries', 'Beer', 'Pizza', 'Soda']

while True:
    order = {
        "section": random.choice(sections),
        "vendor": random.choice(vendors),
        "item": random.choice(items),
        "wait_time": round(random.uniform(1.0, 6.0), 2)
    }

    try:
        res = requests.post(API_URL, json=order)
        print("✅ Order sent:", order)
    except Exception as e:
        print("❌ Failed to send order:", e)

    time.sleep(5)
