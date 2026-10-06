from fastapi import APIRouter, Depends

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/add")
async def add_task():
    return {"message": "Task added successfully"}