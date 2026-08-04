from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

items: List[Item] = [
    Item(id=1, name="Sample Item", description="A starter item", price=9.99),
]

@app.get("/", tags=["General"])
def read_root():
    return {"message": "Welcome to the FastAPI item store!"}

@app.get("/items", response_model=List[Item], tags=["Items"])
def list_items():
    return items

@app.get("/items/{item_id}", response_model=Item, tags=["Items"])
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items", response_model=Item, tags=["Items"])
def create_item(item: Item):
    if any(existing.id == item.id for existing in items):
        raise HTTPException(status_code=400, detail="Item ID already exists")
    items.append(item)
    return item

# Run the app with: uvicorn starter-code:app --reload
