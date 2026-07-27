
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.exceptions import AlreadyExistsError, NotFoundError
from app.users.models import User
from app.users.repository import UserRepository
from app.users.schemas import UserCreate, UserLogin, UserUpdate
from app.users.security import create_access_token, hash_password, verify_password
from jwt import create


class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.repository = UserRepository(db)

    async def create_user(self, user_data: UserCreate) -> User:
        async with self.db.begin():
            existing_user = await self.repository.get_by_mail(user_data.email)

            if existing_user:
                raise AlreadyExistsError(
                    f"this user already exists with mail ID {user_data.email}")

            # hash the password
            user_data.hashed_password = hash_password(
                user_data.hashed_password)
            return await self.repository.create_user(user_data)

    async def get_by_mail(self, email_id: str) -> User:
        user = await self.repository.get_by_mail(email_id)

        if user:
            return user
        raise NotFoundError(f"this email id: {email_id} does not exist")

    async def get_all_users(self) -> list[User]:
        users = await self.repository.get_all()

        if users is None:
            raise NotFoundError(f"No user exist yet")
        return users

    async def update_user(self, upadte_data: UserUpdate, user_id: int) -> User:
        async with self.db.begin():
            user = await self.repository.get_by_id(user_id)

            if user is None:
                raise NotFoundError(f"User not found with this id {user_id}")
            return await self.repository.update_user(upadte_data, user_id)

    async def activate_deactivate_user(self, activation_flag: UserUpdate, user_id: int) -> User:
        async with self.db.begin():
            user = await self.repository.get_by_id(user_id)

            if user is None:
                raise NotFoundError(f"User not found with this id {user_id}")
            return await self.repository.update_user(activation_flag, user_id)

    # async def activate(self, user_id: int) -> User:
    #     async with self.db.begin():
    #         user = await self.repository.get_by_id(user_id)

    #         if user is None:
    #             raise NotFoundError(f"User not found with this id {user_id}")

    #         return await self.repository.activate_user(user_id)

    async def superuser_control(self, superuser_flag: UserUpdate, user_id: int) -> User:
        async with self.db.begin():
            user = await self.repository.get_by_id(user_id)

            if user is None:
                raise NotFoundError(f"User not found with this id {user_id}")
            return await self.repository.update_user(superuser_flag, user_id)


    async def user_login(self,login_data:UserLogin):
        user = await self.repository.get_by_mail(login_data.email)
        if user is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid Email or Password"
            )
        is_valid = verify_password(login_data.password,user.hashed_password)

        if not is_valid:
            raise HTTPException(
                        status_code=401,
                        detail="Invalid Email or Password"
                    )

        access_token = create_access_token(
            subject=str(user.id)
        )


        
