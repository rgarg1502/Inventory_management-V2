from pwdlib import PasswordHash
from datetime import datetime,timedelta,timezone

import jwt

from app.core.config import Settings


password_hash = PasswordHash.recommended()

def hash_password(password:str) -> str:
    return password_hash.hash(password)

def verify_password(plain_password:str, hashed_password:str) -> bool:
    return password_hash.verify(plain_password,hashed_password)

def create_access_token(subject:str) ->str:
    expire = datetime.now(timezone.utc) + timedelta(minutes = Settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    payload = {
        "sub": subject,
        "exp": expire
    }

    token = jwt.encode(
        payload,
        Settings.SECRET_KEY,
        algorithm=Settings.ALGORITHM
    )

    return token

def decode_access_token(token:str) -> dict:
    try:
        payload = jwt.decode(
        token,
        Settings.SECRET_KEY,
        algorithms=[Settings.ALGORITHM]
        )

        return payload
    except jwt.InvalidTokenError:
        return None