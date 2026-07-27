from tkinter import ACTIVE

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import AlreadyExistsError
from .models import User
from .schemas import UserCreate, UserUpdate
from sqlalchemy import select


class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_user(self, user_data: UserCreate) -> User:
        db_user = User(**user_data.model_dump())

        self.db.add(db_user)

        await self.db.flush()

        await self.db.refresh(db_user)

        return db_user

    async def get_by_id(self, user_id: int) -> User:
        stmt = select(User).where(User.id == user_id)

        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()

    async def get_by_mail(self, email: str) -> User:
        stmt = select(User).where(User.email == email)

        result = await self.db.execute(stmt)

        return result.scalar_one_or_none()

    async def get_all(self) -> list[User]:
        stmt = select(User).where(User.is_active == True).order_by(User.id)

        result = await self.db.execute(stmt)

        return result.scalars().all()

    async def update_user(self, user_data: UserUpdate, user_id: int) -> User:
        update_data = user_data.model_dump(exclude_unset=True)
        stmt = select(User).where(User.id == user_id)
        result = await self.db.execute(stmt)
        user = result.scalar_one_or_none()
        if user:
            for key, value in update_data.items():
                setattr(user, key, value)

            await self.db.flush()
            await self.db.refresh(user)

        return user

    # async def activate_user(self, user_id: int) -> User:

    #     stmt = select(User).where(User.id == user_id)
    #     result = await self.db.execute(stmt)
    #     user = result.scalar_one_or_none()
    #     if user:
    #         user.is_active = True
    #     await self.db.flush()
    #     await self.db.refresh(user)
    #     return user
