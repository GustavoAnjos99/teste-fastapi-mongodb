from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from database import *
from usuario import *

router = APIRouter()

@router.post('/')
async def create_usuario_data(usuario: UsuarioSchema = Body(...)):
    usuario = jsonable_encoder(usuario)
    await create_usuario(usuario)
    return "USUARIO CRIADO COM SUCESSO"

@router.delete('/deletar/{usuario}')
async def delete_usuario_data(usuario: str):
    await delete_usuario(usuario)
    return "USUARIO DELETADO COM SUCESSO"