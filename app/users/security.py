from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pwdlib import PasswordHash
from datetime import datetime,timedelta,timezone
from sqlalchemy.ext.asyncio import AsyncSession

import jwt

from app.core.config import settings
from app.database.session import get_db
from app.users.models import User
from app.users.repository import UserRepository


password_hash = PasswordHash.recommended()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")



def hash_password(password:str) -> str:
    return password_hash.hash(password)

def verify_password(plain_password:str, hashed_password:str) -> bool:
    return password_hash.verify(plain_password,hashed_password)



def create_access_token(subject:str) ->str:
    expire = datetime.now(timezone.utc) + timedelta(minutes = settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    payload = {
        "sub": subject,
        "exp": expire
    }

    token = jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return token

def decode_access_token(token:str) -> dict:
    try:
        payload = jwt.decode(
        token,
        settings.SECRET_KEY,
        algorithms=[settings.ALGORITHM]
        )

        return payload
    except jwt.InvalidTokenError:
        return None

async def get_current_user(
        token:str = Depends(oauth2_scheme),
        db: AsyncSession = Depends(get_db)
        ) -> User:
    try:
        payload = decode_access_token(token)

        user_id = payload.get("sub")

        if user_id is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid Credentials"
            )

        repo = UserRepository(db)

        user = await repo.get_by_id(int(user_id))

        if user is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid Credentials"
            )

        return user

    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )
        


    