from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, status, Depends
from app.database.session import get_db
from app.users.models import User
from app.users.schemas import UserCreate, UserResponse, UserUpdate,UserLogin
from app.users.service import UserService


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def user_creation(user_data: UserCreate, db: AsyncSession = Depends(get_db)) -> User:
    service = UserService(db)

    return await service.create_user(user_data)


@router.get("/{email_id}", status_code=status.HTTP_200_OK, response_model=UserResponse)
async def user_by_mail(email_id: str, db: AsyncSession = Depends(get_db)) -> User:
    service = UserService(db)

    return await service.get_by_mail(email_id)


@router.get("", status_code=status.HTTP_200_OK, response_model=list[UserResponse])
async def all_users(db: AsyncSession = Depends(get_db)) -> list[User]:
    service = UserService(db)

    return await service.get_all_users()


@router.patch("/{user_id}", status_code=status.HTTP_200_OK, response_model=UserResponse)
async def user_update(update_data: UserUpdate, user_id: int, db: AsyncSession = Depends(get_db)):
    service = UserService(db)

    return await service.update_user(update_data, user_id)


@router.patch("/{user_id}/activate", status_code=status.HTTP_200_OK, response_model=UserResponse)
async def user_activation_deactivation(activation_flag: UserUpdate, user_id: int, db: AsyncSession = Depends(get_db)):
    service = UserService(db)

    return await service.activate_deactivate_user(activation_flag, user_id)


# @router.patch("/activate/{user_id}", status_code=status.HTTP_200_OK, response_model=UserResponse)
# async def user_activation(user_id: int, db: AsyncSession = Depends(get_db)):
#     service = UserService(db)

#     return await service.activate(user_id)


@router.patch("/{user_id}/superuser", status_code=status.HTTP_200_OK, response_model=UserResponse)
async def control_superuser(superuser_flag: UserUpdate, user_id: int, db: AsyncSession = Depends(get_db)):
    service = UserService(db)

    return await service.activate_deactivate_user(superuser_flag, user_id)

@router.patch("/login",status_code=status.HTTP_202_ACCEPTED)
async def login_user(login_data: UserLogin, db:AsyncSession = Depends(get_db)):
    service = UserService(db)
