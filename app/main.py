from enum import Enum
from fastapi import FastAPI, Response, status
from pydantic import BaseModel
import uvicorn
import asyncio
import json

#Do not forget the dot. 
#When you build a package you have to tell where your class is written using this relative path.
# This is called intra-package references.
from .onebook import NTUNHSLibCrawler

# 這個是建立資料模型 繼承與BaseModel
class Item(BaseModel):
    url: str
    
app = FastAPI()

#c = NTUNHSLibCrawler()
@app.get("/urls/{book_url:path}", status_code=202)
async def crawler(book_url: str):
    #print(book_url)
    book_url=book_url.encode('ascii', 'ignore').decode('unicode_escape')
    crawl = NTUNHSLibCrawler(book_url=book_url)
    if(crawl):
        result = crawl.book
    
    return result

@app.post("/url/", status_code=200)
async def crawler(item: Item, response: Response):# 宣告一個item引數指向Item資料模型
    #print(book_url)
    print(item.url)
    keep = str(item.url.encode('ascii', 'ignore').decode('unicode_escape'))
    crawl = NTUNHSLibCrawler(book_url=keep)
    if(crawl):
        result = crawl.book
    if(result == {"error":"短時間內向北護圖書館發送太多次請求，所以被要求休息一段時間了QQ"}):
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    return result

@app.post("/fake_url/", status_code=202)
async def crawler(item: Item):# 宣告一個item引數指向Item資料模型
    #print(book_url)
    print(item.url)
    keep = str(item.url.encode('ascii', 'ignore').decode('unicode_escape'))
    
    return keep

# 現測試環境採用調式模式執行
#if __name__ == "__main__":
    #uvicorn.run(app, host="0.0.0.0", port=80)