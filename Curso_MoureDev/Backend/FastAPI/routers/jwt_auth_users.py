from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET = "412e6ce05342753a3381e2b2723b86e85ccb5f2e6fe04f6f4832ee107aded32e"

router = APIRouter(prefix="/jwtauth",
                   tags=["jwtauth"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])


class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):
    password: str


users_db = {
    "mouredev": {
        "username": "mouredev",
        "full_name": "Brais Moure",
        "email": "braismoure@mouredev.com",
        "disabled": False,
        "password": "$2a$12$w6N4JV1Wzf/XUJMemsFbgOr3Anc5Q7p1huFOXr1btgYuA2Md034iC"
    },
    "marimar": {
        "username": "marimar",
        "full_name": "Maria del Mar Beiras",
        "email": "marimar492@gmail.com",
        "disabled": True,
        "password": "$2a$12$Tgvs1jXB7d6AoQDb/he6E.iVWXy2z/j8gTqnmN.aNl08mbE9Ia/cm"
    },
}


def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])


def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])


async def auth_user(token: str = Depends(oauth2)):
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales de autenticación inválidas",
        headers={"WWW-Authenticate": "Bearer"})

    try:
        username = jwt.decode(token, SECRET, algorithms=ALGORITHM).get("sub")
        if username is None:
            raise exception

    except JWTError:
        raise exception

    return search_user(username)


async def current_user(user: User = Depends(auth_user)):

    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo")
    return user


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="El usuario no es correcto")

    user = search_user_db(form.username)
    if user is not None:
        if not crypt.verify(form.password, user.password):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="La contraseña no es correcta")

        access_token = {"sub": user.username,
                        "exp":  datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)}

        return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Debe enviar usuario y contraseña")


@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
