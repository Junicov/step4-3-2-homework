from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    number: int


@app.post("/triple")
def triple_number(item: Item):
    return {"result": item.number * 3}
