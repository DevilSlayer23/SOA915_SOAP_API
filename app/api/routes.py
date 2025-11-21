from fastapi import APIRouter
from serivces.user_service import get_user_summary

router = APIRouter()


@router.get("/health")
def health():
    return {"status": "ok"}


@router.get("/users/{user_id}")
def get_user(user_id: int):
    # Example REST wrapper around same business logic
    summary = get_user_summary(user_id)
    return {"data": summary}