### Users DB API ###

from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.client import db_client
from db.schemas.user import user_schema, users_schema
from bson import ObjectId

router = APIRouter(prefix="/userdb",
                   tags=["userdb"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


@router.get("/allusers", response_model=list[User])
async def users():
    return users_schema(db_client.users.find())


@router.get("/{id}")
async def user(id: str):
    return search_user("_id", ObjectId(id))


@router.get("/")
async def userq(id: str):
    return search_user("_id",  ObjectId(id))


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def newuser(user: User):
    if type(search_user("email", user.email)) == User:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="El usuario ya se encuentra registrado")  # se utiliza raise para lanzar la excepcion
    else:
        user_dict = dict(user)
        del user_dict["id"]  # le indico a MongoDb que gestione este campo
        id = db_client.users.insert_one(user_dict).inserted_id

        new_user = user_schema(db_client.users.find_one({"_id": id}))
        return User(**new_user)


@router.put("/", response_model=User)
async def updateuser(user: User):
    user_dict = dict(user)
    del user_dict["id"]

    try:
        db_client.users.find_one_and_replace(
            {"_id": ObjectId(user.id)}, user_dict)
    except:
        return {"error": "No se ha actualizado el usuario"}

    return search_user("_id",  ObjectId(user.id))


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def deleteuser(id: str):
    found = db_client.users.find_one_and_delete({"_id": ObjectId(id)})
    if found:
        return {"Se ha eliminado el usuario"}
    else:
        return {"error": "El usuario no se encuentra"}


def search_user(field: str, key):
    try:
        user = user_schema(db_client.users.find_one({field: key}))
        return User(**user)
    except:
        return {"error": "No existe user con ese id"}
