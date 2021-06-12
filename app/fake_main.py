from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

import asyncio
import json

# 這個是建立資料模型 繼承與BaseModel
class Item(BaseModel):
    url: str
    
app = FastAPI()

@app.post("/fake_url/")
async def crawler(item: Item):# 宣告一個item引數指向Item資料模型
    #print(book_url)
    print(item.url)
    keep = str(item.url.encode('ascii', 'ignore').decode('unicode_escape'))
    
    return keep
