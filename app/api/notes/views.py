from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from .dependencies import get_note_by_id
from .schemas import NoteCreate, NoteRead, NoteUpdate, NoteUpdateParial
from . import crud
from app.dependencies import session_dependency
from app.core.models.notes import Note

router: APIRouter = APIRouter(prefix="/notes", tags=["notes"])


@router.get("/", status_code=status.HTTP_200_OK)
async def get_notes(
    session: AsyncSession = Depends(session_dependency),
) -> list[NoteRead]:
    return await crud.get_notes(session=session)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_note(
    note: NoteCreate,
    session: AsyncSession = Depends(session_dependency),
) -> None:
    await crud.create_note(session=session, note=Note(**note.model_dump()))


@router.get("/{note_id}", status_code=status.HTTP_200_OK)
async def read_note(note: Note = Depends(get_note_by_id)) -> NoteRead:
    return note


@router.put("/{note_id}", status_code=status.HTTP_201_CREATED)
async def update_note(
    note_data: NoteUpdate,
    note: Note = Depends(get_note_by_id),
    session: AsyncSession = Depends(session_dependency),
) -> NoteRead:
    return await crud.update_note(
        session=session,
        note=note,
        data=note_data,
    )


@router.patch("/{note_id}", status_code=status.HTTP_201_CREATED)
async def update_note_partial(
    note_data: NoteUpdateParial,
    note: Note = Depends(get_note_by_id),
    session: AsyncSession = Depends(session_dependency),
) -> NoteRead:
    return await crud.update_note(
        session=session,
        note=note,
        note_update=note_data,
        partial=True,
    )


@router.delete("/{note_id}", status_code=status.HTTP_202_ACCEPTED)
async def delete_note(
    note: Note = Depends(get_note_by_id),
    session: AsyncSession = Depends(session_dependency),
) -> None:
    await crud.delete_note(session=session, note=note)
