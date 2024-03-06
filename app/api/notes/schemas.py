from datetime import datetime
from pydantic import BaseModel, ConfigDict


class NoteRead(BaseModel):
    id: int
    title: str
    content: str | None = None
    created_at: datetime


class NoteCreate(BaseModel):
    title: str
    content: str | None = None

    model_config = ConfigDict(from_attributes=True)


class NoteUpdate(NoteCreate):
    pass


class NoteUpdateParial(BaseModel):
    title: str | None = None
    content: str | None = None

    model_config = ConfigDict(from_attributes=True)
