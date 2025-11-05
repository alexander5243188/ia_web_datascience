# pip install tzdata

from fastapi import FastAPI
from datetime import datetime
import zoneinfo

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


country_timezones = {
    "BO": "America/La_Paz",
    "IN": "Asia/Kolkata",
    "GB": "Europe/London",
    "JP": "Asia/Tokyo",
}


@app.get("/time")
async def real_time():
    return {"current_time": datetime.now()}


@app.get("/time/{iso_code}")
async def read_time(iso_code: str):
    iso = iso_code.upper()
    timezone_str = country_timezones.get(iso)
    tz = zoneinfo.ZoneInfo(timezone_str)
    return {"current_time": datetime.now(tz)}


@app.get("/data/{tipo_hora}")
async def read(tipo_hora: str): 
    return {}