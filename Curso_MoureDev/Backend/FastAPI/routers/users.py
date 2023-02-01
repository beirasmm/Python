from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/users",
                   tags=["users"],
                   responses={404: {"message": "No encontrado"}})

# Entidad user


class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int


users_list = [User(id=1, name="Brais", surname="Moure", url="https//mouredev.com", age=35),
              User(id=2, name="Maria del Mar", surname="Beiras",
                   url="https//mmbeiras.com", age=30),
              User(id=3, name="Marimar", surname="Beiras", url="https//beirasmarimar.com", age=30)]


@router.get("/usersjson")
async def usersjson():
    return [{"name": "Brais", "surname": "Moure", "url_curso": "https//mouredev.com", "age": 35},
            {"name": "Maria del Mar", "surname": "Beiras",
                "url_curso": "https//mmbeiras.com", "age": 30},
            {"name": "Marimar", "surname": "Beiras", "url_curso": "https//beirasmarimar.com", "age": 30}]


@router.get("/users")
async def users():
    return User(id=1, name="Brais", surname="Moure", url="https//mouredev.com", age=30)


@router.get("/userslist")
async def userslist():
    return users_list

# Path (generalmente se utiliza para parametros fijos)


@router.get("/{id}")
async def user(id: int):
    return searchuser(id)


# Query (se utiliza cuando son parametros que no son necesarios en la petición)
@router.get("/userquery/")
async def userquery(id: int):
    return searchuser(id)


def searchuser(id: int):
    user = filter(lambda user: user.id == id, users_list)
    try:
        return list(user)[0]
    except:
        return {"error": "No existe user con ese id"}


# Codigo de respuesta por defecto
@router.post("/user/", response_model=User, status_code=201)
async def newuser(user: User):
    if type(searchuser(user.id)) == User:
        raise HTTPException(status_code=204,
                            detail="El usuario ya se encuentra registrado")  # se utiliza raise para lanzar la excepcion
    else:
        users_list.append(user)
        return user


@router.put("/user/")
async def updateuser(user: User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"error": "El usuario no se encuentra registrado"}
    else:
        return users_list


@router.delete("/user/{id}")
async def deleteuser(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    if found:
        return {"Se ha eliminado el usuario"}
    else:
        return {"error": "El usuario no se encuentra"}
