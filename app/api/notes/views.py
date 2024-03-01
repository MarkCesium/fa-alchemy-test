from fastapi import APIRouter, Depends, HTTPException, status

from .schemas import NoteCreate, NoteRead, NoteUpdate
from . import crud
from app.dependencies import session
from app.core.models.notes import Note

router: APIRouter = APIRouter(prefix="/notes", tags=["notes"])


@router.get("/", status_code=status.HTTP_200_OK)
async def get_notes(
    session=Depends(session),
) -> list[NoteRead]:
    return await crud.get_notes(session=session)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_note(
    note: NoteCreate,
    session=Depends(session),
) -> None:
    await crud.create_note(session=session, note=Note(**note.model_dump()))


@router.get("/{note_id}", status_code=status.HTTP_200_OK)
async def read_note(
    note_id: int,
    session=Depends(session),
):
    note = await crud.get_note(session=session, id=note_id)
    if note == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Note (ID: {note_id}) not found.",
        )
    return note


@router.put("/{note_id}", status_code=status.HTTP_201_CREATED)
async def update_note(
    note_id: int,
    note_data: NoteUpdate,
    session=Depends(session),
) -> None:
    note: Note = await crud.get_note(session=session, id=note_id)
    if note == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Note (ID: {note_id}) not found.",
        )
    await crud.update_note(session=session, note_id=note_id, data=note_data)


@router.delete(
    "/{note_id}",
    status_code=status.HTTP_202_ACCEPTED,
)
async def delete_note(
    note_id: int,
    session=Depends(session),
) -> None:
    note: Note = await crud.get_note(session=session, id=note_id)
    if note == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Note (ID: {note_id}) not found.",
        )
    await crud.delete_note(session=session, note=note)
