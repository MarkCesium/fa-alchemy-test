from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text

from .base import Base


class Note(Base):
    __tablename__ = "notes"

    title: Mapped[str] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Note {self.title} at {self.created_at}>"
