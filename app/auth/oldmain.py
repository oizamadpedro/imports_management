from fastapi import FastAPI
from utils import tools as OSIOTools
from http import HTTPStatus
from routes import auth
from wa_automate_socket_client import SocketClient
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",  # Adicione os domínios permitidos aqui
    "https://seu-outro-dominio.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # ou especifique os métodos permitidos
    allow_headers=["*"],  # ou especifique os cabeçalhos permitidos
)
app.include_router(auth.router, prefix="/auth/v1", tags=["auth"])
