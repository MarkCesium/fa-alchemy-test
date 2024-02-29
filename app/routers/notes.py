from fastapi import APIRouter

router: APIRouter = APIRouter(prefix="/notes", tags=["notes"])


@router.get("/")
async def get_notes():
    pass


@router.post("/")
async def create_note():
    pass


@router.get("/{note_id}")
async def get_note(note_id: int):
    pass


@router.delete("/{note_id}")
async def delete_note(note_id: int):
    pass
