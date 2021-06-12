from enum import Enum
from onebook import NTUNHSLibCrawler
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

import asyncio
import json

# 這個是建立資料模型 繼承與BaseModel
class Item(BaseModel):
    url: str
    
app = FastAPI()

#c = NTUNHSLibCrawler()
@app.get("/urls/{book_url:path}")
async def crawler(book_url: str):
    #print(book_url)
    book_url=book_url.encode('ascii', 'ignore').decode('unicode_escape')
    crawl = NTUNHSLibCrawler(book_url=book_url)
    if(crawl):
        result = crawl.book
    
    return result

@app.post("/url/")
async def crawler(item: Item):# 宣告一個item引數指向Item資料模型
    #print(book_url)
    print(item.url)
    keep = str(item.url.encode('ascii', 'ignore').decode('unicode_escape'))
    crawl = NTUNHSLibCrawler(book_url=keep)
    if(crawl):
        result = crawl.book
    
    return result

@app.post("/fake_url/")
async def crawler(item: Item):# 宣告一個item引數指向Item資料模型
    #print(book_url)
    print(item.url)
    keep = str(item.url.encode('ascii', 'ignore').decode('unicode_escape'))
    
    return keep

# 現測試環境採用調式模式執行
#if __name__ == "__main__":
    #uvicorn.run(app, host="0.0.0.0", port=80)