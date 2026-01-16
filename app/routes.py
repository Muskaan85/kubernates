from fastapi import APIRouter
from app.models import User

router = APIRouter()


@router.get("/users")
def get_users():
    return [
        User(id=1, name="Muskaan"),
        User(id=2, name="Kevin")
    ]
