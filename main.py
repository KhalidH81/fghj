from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import models, schemas, crud
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Widget CRUD API", version="1.0")

@app.post("/widgets/", response_model=schemas.Widget)
def create_widget(widget: schemas.WidgetCreate, db: Session = Depends(get_db)):
    return crud.create_widget(db=db, widget=widget)

@app.get("/widgets/{widget_id}", response_model=schemas.Widget)
def read_widget(widget_id: int, db: Session = Depends(get_db)):
    db_widget = crud.get_widget(db, widget_id)
    if not db_widget:
        raise HTTPException(status_code=404, detail="Widget not found")
    return db_widget

@app.get("/widgets/", response_model=List[schemas.Widget])
def list_widgets(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.list_widgets(db, skip=skip, limit=limit)

@app.put("/widgets/{widget_id}", response_model=schemas.Widget)
def update_widget(widget_id: int, widget: schemas.WidgetUpdate, db: Session = Depends(get_db)):
    db_widget = crud.update_widget(db, widget_id, widget)
    if not db_widget:
        raise HTTPException(status_code=404, detail="Widget not found")
    return db_widget

@app.delete("/widgets/{widget_id}")
def delete_widget(widget_id: int, db: Session = Depends(get_db)):
    if not crud.delete_widget(db, widget_id):
        raise HTTPException(status_code=404, detail="Widget not found")
    return {"detail": "Widget deleted"}
