from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)


async def get_current_user(
    token: str = Depends(oauth2_scheme)
):
    return token