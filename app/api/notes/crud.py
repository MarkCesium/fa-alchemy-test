from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy import select
from sqlalchemy.engine import Result

from app.core.models.notes import Note
from .schemas import NoteUpdate, NoteUpdateParial


async def get_notes(session: async_sessionmaker[AsyncSession]) -> list[Note]:
    async with session() as sess:
        query = select(Note).order_by(Note.id)
        result: Result = await sess.execute(query)
        return result.scalars()


async def get_note(session: async_sessionmaker[AsyncSession], id: int) -> Note | None:
    async with session() as sess:
        return await sess.get(Note, id)


async def create_note(session: async_sessionmaker[AsyncSession], note: Note) -> None:
    async with session() as sess:
        sess.add(note)
        await sess.commit()


async def update_note(
    session: async_sessionmaker[AsyncSession],
    note_id: int,
    data: NoteUpdate | NoteUpdateParial,
    partial: bool = False,
) -> Note:
    async with session() as sess:
        note = await sess.get(Note, note_id)
        for name, value in data.model_dump(exclude_unset=partial).items():
            setattr(note, name, value)
        await sess.commit()
        return note


async def delete_note(session: async_sessionmaker[AsyncSession], note: Note):
    async with session() as sess:
        await sess.delete(note)
        await sess.commit()
