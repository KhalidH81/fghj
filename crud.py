from sqlalchemy.orm import Session
import models, schemas

def create_widget(db: Session, widget: schemas.WidgetCreate):
    db_widget = models.Widget(**widget.dict())
    db.add(db_widget)
    db.commit()
    db.refresh(db_widget)
    return db_widget

def get_widget(db: Session, widget_id: int):
    return db.query(models.Widget).filter(models.Widget.id == widget_id).first()

def list_widgets(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Widget).offset(skip).limit(limit).all()

def update_widget(db: Session, widget_id: int, widget: schemas.WidgetUpdate):
    db_widget = get_widget(db, widget_id)
    if not db_widget:
        return None
    for key, value in widget.dict().items():
        setattr(db_widget, key, value)
    db.commit()
    db.refresh(db_widget)
    return db_widget

def delete_widget(db: Session, widget_id: int):
    db_widget = get_widget(db, widget_id)
    if not db_widget:
        return False
    db.delete(db_widget)
    db.commit()
    return True
