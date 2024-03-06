from fastapi import Path, Depends, HTTPException, status
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import session_dependency
from app.core.models import Note
from . import crud


async def get_note_by_id(
    note_id: Annotated[int, Path],
    session: AsyncSession = Depends(session_dependency),
) -> Note:
    note = await crud.get_note(session=session, id=note_id)
    if note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Note (ID: {note_id}) not found.",
        )

    return note
