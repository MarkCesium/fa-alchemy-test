from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy import select
from sqlalchemy.engine import Result

from app.core.models.notes import Note
from .schemas import NoteUpdate, NoteUpdateParial


async def get_notes(session: AsyncSession) -> list[Note]:
    query = select(Note).order_by(Note.id)
    result: Result = await session.execute(query)
    return result.scalars()


# It in use in dependencies.py
async def get_note(session: AsyncSession, id: int) -> Note | None:
    return await session.get(Note, id)


async def create_note(session: AsyncSession, note: Note) -> None:
    session.add(note)
    await session.commit()


async def update_note(
    session: AsyncSession,
    note: Note,
    note_update: NoteUpdate | NoteUpdateParial,
    partial: bool = False,
) -> Note:
    for name, value in note_update.model_dump(exclude_unset=partial).items():
        setattr(note, name, value)
    await session.commit()

    return note


async def delete_note(session: AsyncSession, note: Note):
    await session.delete(note)
    await session.commit()
