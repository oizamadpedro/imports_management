from fastapi import APIRouter
from osio.services.UserService import UserService
from osio.base.baseModels import User
from hashlib import sha256

router = APIRouter()
salt_password = "s3nh4Sup3$$$rS$#!ECRETA"

@router.get("/")
async def getUsers():
    users = UserService.get()
    return {'data': users}

@router.post("/")
async def createUser(user: User):
    if UserService.usernameExists(user):
        return {'error': 'username exists'}
    else:
        password = salt_password + user.password
        user.password = sha256(password.encode()).hexdigest()
        userCreated = UserService.post(user)
        return {'message': 'user created.', 'data': userCreated}
    